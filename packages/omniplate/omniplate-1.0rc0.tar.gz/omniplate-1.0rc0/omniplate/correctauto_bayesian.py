# A Bayesian version of the method in Lichten ... Swain, BMC Biophys 2014
# TODO
# why is the predicted fluorescence so low? refstrain at wrong OD?
# delete code on priors - no longer used; general tidy
import numpy as np
from scipy.optimize import minimize
from tqdm import tqdm

import omniplate.corrections as omcorr
import omniplate.omgenutils as gu
import omniplate.sunder as sunder
from omniplate.runfitderiv import runfitderiv

rng = np.random.default_rng()

# notation follows Lichten ... Swain
# GFP is denoted y; AutoFL is denoted z.
# The reference strain is denoted WT.


def de_nan(y, z):
    """Remove any replicates with NaN."""
    # NaNs are generated because experiments have different durations
    keep = ~np.any(np.isnan(y), axis=0)
    return y[:, keep], z[:, keep]


def sample_b(nosamples, bdata):
    """Sample background fluorescence."""
    s2 = np.var(bdata) / bdata.size
    u = np.mean(bdata)
    samples = u + s2 * rng.standard_normal(nosamples)
    if np.any(samples < 0):
        print("Warning: negative background fluorescence.")
    return samples


def get_background_samples(yn, zn, nosamples):
    """Get samples of background fluorescence for GFP and AutoFL."""
    by = sample_b(nosamples, yn)
    bz = sample_b(nosamples, zn)
    return by, bz


def set_up(y, z, ywt, zwt, yn, zn):
    """Define stats_dict."""
    # raguess = np.max((zwt - np.median(zn)) / (ywt - np.median(yn)), axis=1)
    # raguess = raguess[~np.isinf(raguess)]
    stats_dict = {
        "x0": None,
        "gmax": np.max(y),
        "amax": np.max(ywt),
        "ramin": 0,  # np.min(raguess[raguess > 0]),
        "ramax": 1,  # np.max(raguess[raguess > 0]),
        "seq_prior_mu": None,
        "seq_prior_hess": None,
    }
    return stats_dict


def minus_log_prob_array(theta, stats_dict):
    """Get log normal probability."""
    g, ra, a = theta
    rg = stats_dict["rg"]
    n = stats_dict["n"]
    sy = stats_dict["sy"]
    sz = stats_dict["sz"]
    sywt = stats_dict["sywt"]
    szwt = stats_dict["szwt"]
    by = stats_dict["by"]
    bz = stats_dict["bz"]
    bywt = stats_dict["by"]
    bzwt = stats_dict["bz"]
    ly = stats_dict["ly"]
    lz = stats_dict["lz"]
    lywt = stats_dict["lywt"]
    lzwt = stats_dict["lzwt"]
    mlp_v = np.sum(
        n * np.log(sy * sz * sywt * szwt)
        + (np.log(a + g + by) - ly) ** 2 / (2 * sy**2)
        + (np.log(a * ra + g * rg + bz) - lz) ** 2 / (2 * sz**2)
        + (np.log(a + bywt) - lywt) ** 2 / (2 * sywt**2)
        + (np.log(a * ra + bzwt) - lzwt) ** 2 / (2 * szwt**2),
        axis=0,
    )
    return mlp_v


def minus_log_prob(theta, stats_dict):
    """Find joint probability averaged over background fluorescence."""
    mlp_v = minus_log_prob_array(theta, stats_dict)
    mlp = average_background_fluorescence(mlp_v)
    return mlp


def average_background_fluorescence(mlp, deriv=None):
    """Average background fluorescence."""
    norm = np.min(mlp)
    # normalise to prevent underflows, exponentiate, then average
    norm_prob = np.exp(norm - mlp)
    if deriv is None:
        # revert normalisation and return -log(probability)
        minus_log_prob = norm - np.log(np.mean(norm_prob))
        return minus_log_prob
    else:
        # return weighted average of a derivative array
        deriv_average = np.sum(deriv * norm_prob) / np.sum(norm_prob)
        return deriv_average


def jac_arrays(theta, stats_dict):
    """Get Jacobian of log normal probability."""
    g, ra, a = theta
    rg = stats_dict["rg"]
    sy = stats_dict["sy"]
    sz = stats_dict["sz"]
    sywt = stats_dict["sywt"]
    szwt = stats_dict["szwt"]
    by = stats_dict["by"]
    bz = stats_dict["bz"]
    bywt = stats_dict["by"]
    bzwt = stats_dict["bz"]
    ly = stats_dict["ly"]
    lz = stats_dict["lz"]
    lywt = stats_dict["lywt"]
    lzwt = stats_dict["lzwt"]
    jac_v = np.zeros(3, dtype="object")
    y_v = (np.log(a + g + by) - ly) / (sy**2 * (a + g + by))
    z_v = (np.log(a * ra + g * rg + bz) - lz) / (
        sz**2 * (a * ra + g * rg + bz)
    )
    ywt_v = (np.log(a + bywt) - lywt) / (sywt**2 * (a + bywt))
    zwt_v = (np.log(a * ra + bzwt) - lzwt) / (szwt**2 * (a * ra + bzwt))
    # with respect to g
    jac_v[0] = np.sum(y_v + rg * z_v, axis=0)
    # with respect to ra
    jac_v[1] = np.sum(a * (z_v + zwt_v), axis=0)
    # with respect to a
    jac_v[2] = np.sum(y_v + ywt_v + ra * (z_v + zwt_v), axis=0)
    return jac_v


def jac(theta, stats_dict, return_jac_v=False):
    """Get Jacobian averaged over background fluorescence."""
    jac_v = jac_arrays(theta, stats_dict)
    # average background fluorescence
    mlp_v = minus_log_prob_array(theta, stats_dict)
    av_jac = np.array(
        [average_background_fluorescence(mlp_v, jac_v[i]) for i in range(3)]
    )
    if return_jac_v:
        return av_jac, jac_v
    else:
        return av_jac


def hess_arrays(theta, stats_dict):
    """Get Hessian of log normal probability."""
    g, ra, a = theta
    rg = stats_dict["rg"]
    sy = stats_dict["sy"]
    sz = stats_dict["sz"]
    sywt = stats_dict["sywt"]
    szwt = stats_dict["szwt"]
    by = stats_dict["by"]
    bz = stats_dict["bz"]
    bywt = stats_dict["by"]
    bzwt = stats_dict["bz"]
    ly = stats_dict["ly"]
    lz = stats_dict["lz"]
    lywt = stats_dict["lywt"]
    lzwt = stats_dict["lzwt"]
    hess_v = np.zeros((3, 3), dtype="object")
    y_v = (1 - np.log(a + g + by) + ly) / (sy**2 * (a + g + by) ** 2)
    z_v = (1 - np.log(a * ra + g * rg + bz) + lz) / (
        sz**2 * (a * ra + g * rg + bz) ** 2
    )
    ywt_v = (1 - np.log(a + bywt) + lywt) / (sywt**2 * (a + bywt) ** 2)
    zwt_v = (1 - np.log(a * ra + bzwt) + lzwt) / (
        szwt**2 * (a * ra + bzwt) ** 2
    )
    z_vv = (np.log(a * ra + g * rg + bz) - lz) / (
        sz**2 * (a * ra + g * rg + bz)
    )
    zwt_vv = (np.log(a * ra + bzwt) - lzwt) / (szwt**2 * (a * ra + bzwt))
    # g, g
    hess_v[0, 0] = y_v + rg**2 * z_v
    # ra, ra
    hess_v[1, 1] = a**2 * (z_v + zwt_v)
    # a, a
    hess_v[2, 2] = y_v + ywt_v + ra**2 * (z_v + zwt_v)
    # g, ra
    hess_v[0, 1] = a * rg * z_v
    # g, a
    hess_v[0, 2] = y_v + ra * rg * z_v
    # ra, a
    hess_v[1, 2] = a * ra * (z_v + zwt_v) + z_vv + zwt_vv
    # sum over replicates
    for i in range(3):
        for j in range(i, 3):
            hess_v[i, j] = np.sum(hess_v[i, j], axis=0)
            if j > i:
                hess_v[j, i] = hess_v[i, j]
    return hess_v


def hess(theta, stats_dict):
    """Get Hessian averaged over background fluorescence."""
    mlp_v = minus_log_prob_array(theta, stats_dict)
    av_jac, jac_v = jac(theta, stats_dict, return_jac_v=True)
    hess_v = hess_arrays(theta, stats_dict)
    av_hess = np.empty((3, 3))
    for i in range(3):
        for j in range(i, 3):
            av_hess[i, j] = (
                average_background_fluorescence(mlp_v, hess_v[i, j])
                + av_jac[i] * av_jac[j]
                - average_background_fluorescence(mlp_v, jac_v[i] * jac_v[j])
            )
            if j > i:
                av_hess[j, i] = av_hess[i, j]
    return av_hess


def minus_log_prior(theta, stats_dict):
    """Get minus log of the prior probability."""
    g, ra, a = theta
    mlp = 0
    if stats_dict["seq_prior_hess"] is not None:
        mu = stats_dict["seq_prior_mu"]
        h = stats_dict["seq_prior_hess"]
        mlp = (
            (g - mu[0]) ** 2 * h[0, 0]
            + 2 * (g - mu[0]) * (ra - mu[1]) * h[0, 1]
            + 2 * (g - mu[0]) * (a - mu[2]) * h[0, 2]
            + (ra - mu[1]) ** 2 * h[1, 1]
            + 2 * (ra - mu[1]) * (a - mu[2]) * h[1, 2]
            + (a - mu[2]) ** 2 * h[2, 2]
        ) / 2
    return mlp


def jac_prior(theta, stats_dict):
    """Get Jacobian for -log prior."""
    g, ra, a = theta
    jac = np.zeros(3)
    if stats_dict["seq_prior_mu"] is not None:
        mu = stats_dict["seq_prior_mu"]
        h = stats_dict["seq_prior_hess"]
        jac[0] = (
            g * h[0, 0]
            + a * h[0, 2]
            - h[0, 0] * mu[0]
            - h[0, 1] * mu[1]
            - h[0, 2] * mu[2]
            + h[0, 1] * ra
        )
        jac[1] = (
            g * h[0, 1]
            + a * h[1, 2]
            - h[0, 1] * mu[0]
            - h[1, 1] * mu[1]
            - h[1, 2] * mu[2]
            + h[1, 1] * ra
        )
        jac[2] = (
            g * h[0, 2]
            + a * h[2, 2]
            - h[0, 2] * mu[0]
            - h[1, 2] * mu[1]
            - h[2, 2] * mu[2]
            + h[1, 2] * ra
        )
    return jac


def hess_prior(theta, stats_dict):
    """Get Hessian for -log prior."""
    hess = np.zeros((3, 3))
    if stats_dict["seq_prior_hess"] is not None:
        hess = stats_dict["seq_prior_hess"]
    return hess


def set_up_minimization(stats_dict):
    """Set up bounds and initial guess."""
    g_bounds = (0, stats_dict["gmax"])
    ra_bounds = (stats_dict["ramin"], stats_dict["ramax"])
    a_bounds = (0, stats_dict["amax"])
    bounds = [g_bounds, ra_bounds, a_bounds]
    x0_o = np.array(
        [
            np.median(np.exp(stats_dict["ly"])),
            np.median(np.exp(stats_dict["lzwt"] - stats_dict["lywt"])),
            np.median(np.exp(stats_dict["lywt"])),
        ]
    )
    if stats_dict["x0"] is None:
        x0 = x0_o
    else:
        x0 = stats_dict["x0"]
    return bounds, x0, x0_o


def find_mode(stats_dict, no_attempts, prior=False):
    """
    Find most probable value of g and ra.

    Tried with a sequential approach, using the a Gaussian
    approximation of the current posterior as the prior
    for the future one, but performs worse, perhaps because
    of the wide hessian.
    """
    bounds, x0, x0_o = set_up_minimization(stats_dict)
    min_mlp = np.inf
    mode = None
    rands = rng.standard_normal((no_attempts, 3))
    for i in range(no_attempts):
        if i < int(no_attempts / 2):
            # start from proceeding optimum
            sampled_x0 = rands[i, :] * 10 * np.sqrt(x0) + x0
        else:
            # start from a new guess
            sampled_x0 = rands[i, :] * 10 * np.sqrt(x0_o) + x0_o
        sampled_x0[sampled_x0 < 0] = 0.01
        if prior:
            res = minimize(
                lambda x: minus_log_prob(x, stats_dict)
                + minus_log_prior(x, stats_dict),
                x0=sampled_x0,
                bounds=bounds,
                jac=lambda x: jac(x, stats_dict) + jac_prior(x, stats_dict),
                hess=lambda x: hess(x, stats_dict) + hess_prior(x, stats_dict),
                method="L-BFGS-B",
            )
        else:
            res = minimize(
                lambda x: minus_log_prob(x, stats_dict),
                x0=sampled_x0,
                bounds=bounds,
                jac=lambda x: jac(x, stats_dict),
                hess=lambda x: hess(x, stats_dict),
                method="L-BFGS-B",
            )
        if res.success:
            if res.fun < min_mlp:
                mode = res.x
                min_mlp = res.fun
                stats_dict["x0"] = res.x
                hit_boundary = [
                    j
                    for j in range(3)
                    if mode[j] == bounds[j][0] or mode[j] == bounds[j][1]
                ]
                if not hit_boundary:
                    # update prior following sequential bayes
                    stats_dict["seq_prior_mu"] = res.x
                    stats_dict["seq_prior_hess"] = hess(res.x, stats_dict)
    if mode is None:
        print(" Warning: Maximising posterior probability failed.")
        mode = np.nan * np.ones(3)
        stats_dict["x0"] = None
    return mode


def correctauto_bayesian(
    self,
    f,
    refstrain,
    flcvfn,
    bd,
    max_data_pts,
    nosamples_for_bg,
    no_minimisation_attempts,
    nosamples,
    experiments,
    experimentincludes,
    experimentexcludes,
    conditions,
    conditionincludes,
    conditionexcludes,
    strains,
    strainincludes,
    strainexcludes,
):
    """
    Correct fluorescence for auto- and background fluorescence.

    Use a Bayesian method to correct for autofluorescence from fluorescence
    measurements at two wavelengths and for background fluorescence.

    Implement demixing following Lichten ... Swain, BMC Biophys 2014.

    Integrate over autofluorescence exactly and other nuisance variable
    by sampling.
    """
    print("Using Bayesian approach for two fluorescence wavelengths.")
    print(f"Correcting autofluorescence using {f[0]} and {f[1]}.")
    bname = "bc" + f[0]
    bd_default = {0: (-2, 8), 1: (-2, 4), 2: (-4, 6)}
    if bd is not None:
        bdn = gu.mergedicts(original=bd_default, update=bd)
    else:
        bdn = bd_default
    for e in sunder.getset(
        self,
        experiments,
        experimentincludes,
        experimentexcludes,
        "experiment",
        nonull=True,
    ):
        for c in sunder.getset(
            self,
            conditions,
            conditionincludes,
            conditionexcludes,
            labeltype="condition",
            nonull=True,
            nomedia=True,
        ):
            # get data for reference strain
            # y for emission at 525; z for emission at 585
            _, (ywt, zwt) = sunder.extractwells(
                self.r, self.s, e, c, refstrain, f
            )
            ywt, zwt = de_nan(ywt, zwt)
            # get data for Null
            _, (yn, zn) = sunder.extractwells(self.r, self.s, e, c, "Null", f)
            yn, zn = de_nan(yn, zn)
            # check sufficient replicates
            if (ywt.shape[1] < 3) or (yn.shape[1] < 3):
                raise Exception(
                    f"There are less than three replicates for the {refstrain}"
                    " or Null strains."
                )
            for s in sunder.getset(
                self,
                strains,
                strainincludes,
                strainexcludes,
                labeltype="strain",
                nonull=True,
            ):
                if (
                    s != refstrain
                    and f"{s} in {c}" in self.allstrainsconditions[e]
                ):
                    # get data for tagged strain
                    t, (y, z, od) = sunder.extractwells(
                        self.r, self.s, e, c, s, f.copy() + ["OD"]
                    )
                    y, z = de_nan(y, z)
                    if y.size == 0 or z.size == 0:
                        print(f"Warning: No data found for {e}: {s} in {c}!!")
                        continue
                    if y.shape[1] < 3:
                        raise Exception(
                            "There are less than three replicates"
                            f" for {e}: {s} in {c}."
                        )
                    print(f"{e}: {s} in {c}")
                    # correct autofluorescence for each time point
                    predicted_fl = np.zeros(t.size)
                    stats_dict = set_up(y, z, ywt, zwt, yn, zn)
                    stats_dict["rg"] = self._gamma
                    stats_dict["n"] = y.shape[1]
                    for i in tqdm(range(t.size)):
                        stats_dict["by"], stats_dict["bz"] = (
                            get_background_samples(
                                yn[i, :], zn[i, :], nosamples_for_bg
                            )
                        )
                        stats_dict["sy"] = np.std(np.log(y[i, :]))
                        stats_dict["sz"] = np.std(np.log(z[i, :]))
                        stats_dict["sywt"] = np.std(np.log(ywt[i, :]))
                        stats_dict["szwt"] = np.std(np.log(zwt[i, :]))
                        stats_dict["ly"] = np.log(y[i, :])[:, None]
                        stats_dict["lz"] = np.log(z[i, :])[:, None]
                        stats_dict["lywt"] = np.log(ywt[i, :])[:, None]
                        stats_dict["lzwt"] = np.log(zwt[i, :])[:, None]
                        posterior_mode = find_mode(
                            stats_dict, no_minimisation_attempts
                        )
                        predicted_fl[i] = posterior_mode[0]
                    # smooth with GP and add to data frames
                    print("Smoothing...")
                    flgp, _ = runfitderiv(
                        self,
                        t,
                        predicted_fl,
                        f"{bname}",
                        f"d/dt_{bname}",
                        experiment=e,
                        condition=c,
                        strain=s,
                        bd=bdn,
                        cvfn=flcvfn,
                        logs=False,
                        figs=True,
                        plotlocalmax=False,
                        max_data_pts=max_data_pts,
                    )
                    # sample ODs using GPs
                    lod_samples = omcorr.sample_ODs_with_GP(
                        self, e, c, s, t, od, nosamples
                    )
                    od_samples = np.exp(lod_samples)
                    # find samples of fluorescence per OD
                    smooth_fl_samples = flgp.fitderivsample(nosamples)[0]
                    flperod = smooth_fl_samples / od_samples
                    # store results for fluorescence per OD
                    autofdict = {
                        "experiment": e,
                        "condition": c,
                        "strain": s,
                        "time": t,
                        f"{bname}perOD": np.mean(flperod, 1),
                        f"{bname}perOD_err": omcorr.nanstdzeros2nan(
                            flperod, 1
                        ),
                    }
                    # add to data frames
                    omcorr.addtodataframes(self, autofdict, bname)
