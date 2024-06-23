import numpy as np
import pandas as pd

from mirp.settings.feature_parameters import FeatureExtractionSettingsClass
from mirp._images.generic_image import GenericImage
from mirp._images.transformed_image import TransformedImage
from mirp._masks.base_mask import BaseMask


def get_intensity_volume_histogram_features(
        image: GenericImage,
        mask: BaseMask,
        settings: FeatureExtractionSettingsClass
) -> pd.DataFrame:
    """
    Extract intensity-volume histogram features for the given mask.
    """

    # Create intensity-volume histogram
    df_ivh, n_bins = get_intensity_volume_histogram(
        image=image,
        mask=mask,
        settings=settings
    )

    # Extract intensity volume histogram features from the intensity volume histogram
    df_feat = compute_intensity_volume_histogram_features(
        df_ivh=df_ivh,
        n_bins=n_bins,
        settings=settings
    )

    return df_feat


def get_intensity_volume_histogram(
        image: GenericImage,
        mask: BaseMask,
        settings: FeatureExtractionSettingsClass
) -> tuple[None | pd.DataFrame, int]:
    """
    Determines the intensity-volume histogram (IVH) for the given mask.
    """
    import copy
    from mirp._images.ct_image import CTImage
    from mirp._images.pet_image import PETImage

    # Convert image volume to table
    df_img = mask.as_pandas_dataframe(image=image, intensity_mask=True)

    # Skip further processing if df_img is None due to missing input image and/or ROI
    if df_img is None:
        return None, 0

    # Remove voxels outside roi
    df_his = df_img[df_img.roi_int_mask == True].copy()

    # Check if the roi histogram contains any voxels
    if len(df_his) == 0:
        return None, 0

    # Get number of voxels in the image
    n_v = len(df_his)

    # Get the range of grey levels
    if mask.intensity_range is None:
        g_range_loc = np.array([np.nan, np.nan])
    else:
        g_range_loc = copy.deepcopy(np.array(mask.intensity_range))

    # Get the discretisation method
    if isinstance(image, TransformedImage):
        ivh_discr_method = "fixed_bin_number"
    else:
        ivh_discr_method = settings.ivh_discretisation_method

    # Set missing discretisation methods based on modality
    if ivh_discr_method == "none":
        if isinstance(image, CTImage):
            pass
        elif isinstance(image, PETImage):
            ivh_discr_method = "fixed_bin_size"
        else:
            levels = np.unique(df_his.g)
            if np.all(np.fmod(levels, 1.0) == 0.0):
                ivh_discr_method = "none"
            else:
                ivh_discr_method = "fixed_bin_number"

    if ivh_discr_method == "none":
        # Calculation without transformation

        # Update grey level range when the range is not (completely) provided
        if np.isnan(g_range_loc[0]):
            g_range_loc[0] = np.min(df_his.g) * 1.0
        if np.isnan(g_range_loc[1]):
            g_range_loc[1] = np.max(df_his.g) * 1.0

        # Set number of bins. The number of bins is equal to the number of grey levels present
        n_bins = g_range_loc[1] - g_range_loc[0] + 1.0

        # Create histogram by grouping by intensity level and counting bin size
        df_his = df_his.groupby(by="g").size().reset_index(name="n")

        # Append empty grey levels to histogram
        levels = np.arange(start=g_range_loc[0], stop=g_range_loc[1] + 1)
        miss_level = levels[np.logical_not(np.isin(levels, df_his.g))]
        n_miss = len(miss_level)
        if n_miss > 0:
            df_his = pd.concat(
                [df_his, pd.DataFrame({"g": miss_level, "n": np.zeros(n_miss)})],
                ignore_index=True)

        del levels, miss_level, n_miss

    elif ivh_discr_method == "fixed_bin_size":
        # Fixed bin size/width calculations

        # Update grey level range when the range is not (completely) provided
        if np.isnan(g_range_loc[0]):
            g_range_loc[0] = np.min(df_his.g) * 1.0
        if np.isnan(g_range_loc[1]):
            g_range_loc[1] = np.max(df_his.g) * 1.0

        # Set bin width and get the number of bins required
        bin_width = settings.ivh_discretisation_bin_width

        # Set missing bin width based on the modality
        if bin_width is None:
            if isinstance(image, CTImage):
                bin_width = 1.0
            elif isinstance(image, PETImage):
                bin_width = 0.1
            else:
                raise ValueError("bin_width has not been set.")

        # Get the number of bins
        n_bins = np.ceil((g_range_loc[1] - g_range_loc[0]) / bin_width) + 1.0

        # Bin voxels
        df_his.g = np.floor((df_his.g - g_range_loc[0]) / (bin_width * 1.0)) + 1.0

        # Set voxels with grey level lower than 0.0 to 1.0. This may occur with non-mask voxels
        # and voxels with the minimum intensity
        df_his.loc[df_his["g"] <= 0.0, "g"] = 1.0

        # Create histogram by grouping by intensity level and counting bin size
        df_his = df_his.groupby(by="g").size().reset_index(name="n")

        # Append empty grey levels to histogram
        levels = np.arange(start=1, stop=n_bins+1)
        miss_level = levels[np.logical_not(np.isin(levels, df_his.g))]
        n_miss = len(miss_level)
        if n_miss > 0:
            df_his = pd.concat(
                [df_his, pd.DataFrame({"g": miss_level, "n": np.zeros(n_miss)})],
                ignore_index=True)

        del levels, miss_level, n_miss

        # Replace g by the bin centers
        df_his.loc[:, "g"] = g_range_loc[0] + (df_his["g"] - 0.5) * bin_width * 1.0

        # Update grey level range
        g_range_loc[0] = np.min(df_his.g)
        g_range_loc[1] = np.max(df_his.g)

    elif ivh_discr_method == "fixed_bin_number":
        # Calculation for all other image types

        # Set grey level range
        g_range_loc[0] = np.min(df_his.g) * 1.0
        g_range_loc[1] = np.max(df_his.g) * 1.0

        # Set bin size and number of bins
        n_bins = settings.ivh_discretisation_n_bins

        # Set missing number of bins
        if n_bins is None:
            n_bins = 1000.0

        # Update grey level range
        df_his.loc[:, "g"] = np.floor(n_bins * (df_his["g"] - g_range_loc[0]) / (g_range_loc[1] - g_range_loc[0])) + 1.0

        # Update values at the boundaries
        df_his.loc[df_his["g"] <= 0.0, "g"] = 1.0
        df_his.loc[df_his["g"] >= n_bins * 1.0, "g"] = n_bins * 1.0

        # Create histogram by grouping by intensity level and counting bin size
        df_his = df_his.groupby(by="g").size().reset_index(name="n")

        # Append empty grey levels to histogram
        levels = np.arange(start=1, stop=n_bins + 1)
        miss_level = levels[np.logical_not(np.isin(levels, df_his.g))]
        n_miss = len(miss_level)
        if n_miss > 0:
            df_his = pd.concat(
                [df_his, pd.DataFrame({"g": miss_level, "n": np.zeros(n_miss)})],
                ignore_index=True)

        del levels, miss_level, n_miss

        # Update grey level range
        g_range_loc[0] = 1.0
        g_range_loc[1] = n_bins
    else:
        raise ValueError(f"{ivh_discr_method} is not a valid IVH discretisation method.")

    # Order histogram table by increasing grey level
    df_his = df_his.sort_values(by="g")

    # Calculate intensity fraction
    df_his["gamma"] = (df_his.g - g_range_loc[0]) / (g_range_loc[1] - g_range_loc[0])

    # Calculate volume fraction
    df_his["nu"] = 1.0 - (np.cumsum(np.append([0], df_his.n))[0:int(n_bins)]) * 1.0 / (n_v * 1.0)

    return df_his, n_bins


def compute_intensity_volume_histogram_features(
        df_ivh: None | pd.DataFrame,
        n_bins: int,
        settings: FeatureExtractionSettingsClass
):
    """
    Definitions of intensity-volume histogram features
    :param df_ivh: intensity volume histogram as created using the get_intensity_volume_histogram function
    :param n_bins: number of bins in the histogram
    :param settings: Set of settings.
    :return: pandas DataFrame with feature values
    """

    # Create feature table
    feat_names = ["ivh_v10", "ivh_v25", "ivh_v50", "ivh_v75", "ivh_v90",
                  "ivh_i10", "ivh_i25", "ivh_i50", "ivh_i75", "ivh_i90",
                  "ivh_diff_v10_v90", "ivh_diff_v25_v75", "ivh_diff_i10_i90", "ivh_diff_i25_i75"]

    if not settings.ibsi_compliant:
        feat_names += ["ivh_auc"]

    df_feat = pd.DataFrame(np.full(shape=(1, len(feat_names)), fill_value=np.nan))
    df_feat.columns = feat_names

    if df_ivh is None:
        return df_feat

    # Volume fraction at 10% intensity
    v10 = df_ivh.loc[df_ivh.gamma >= 0.10, :].nu.max()
    df_feat["ivh_v10"] = v10

    # Volume fraction at 25% intensity
    v25 = df_ivh.loc[df_ivh.gamma >= 0.25, :].nu.max()
    df_feat["ivh_v25"] = v25

    # Volume fraction at 50% intensity
    v50 = df_ivh.loc[df_ivh.gamma >= 0.50, :].nu.max()
    df_feat["ivh_v50"] = v50

    # Volume fraction at 75% intensity
    v75 = df_ivh.loc[df_ivh.gamma >= 0.75, :].nu.max()
    df_feat["ivh_v75"] = v75

    # Volume fraction at 90% intensity
    v90 = df_ivh.loc[df_ivh.gamma >= 0.90, :].nu.max()
    df_feat["ivh_v90"] = v90

    # Intensity at 10% volume
    i10 = df_ivh.loc[df_ivh.nu <= 0.10, :].g.min()
    if np.isnan(i10):
        i10 = n_bins + 1.0
    df_feat["ivh_i10"] = i10

    # Intensity at 25% volume
    i25 = df_ivh.loc[df_ivh.nu <= 0.25, :].g.min()
    if np.isnan(i25):
        i25 = n_bins + 1.0
    df_feat["ivh_i25"] = i25

    # Intensity at 50% volume
    i50 = df_ivh.loc[df_ivh.nu <= 0.50, :].g.min()
    if np.isnan(i50):
        i50 = n_bins + 1.0
    df_feat["ivh_i50"] = i50

    # Intensity at 75% volume
    i75 = df_ivh.loc[df_ivh.nu <= 0.75, :].g.min()
    if np.isnan(i75):
        i75 = n_bins + 1.0
    df_feat["ivh_i75"] = i75

    # Intensity at 90% volume
    i90 = df_ivh.loc[df_ivh.nu <= 0.90, :].g.min()
    if np.isnan(i90):
        i90 = n_bins + 1.0
    df_feat["ivh_i90"] = i90

    # Difference in volume fraction between 10% and 90% intensity
    df_feat["ivh_diff_v10_v90"] = v10 - v90

    # Difference in volume fraction between 25% and 75% intensity
    df_feat["ivh_diff_v25_v75"] = v25 - v75

    # Difference in intensity between 10% and 90% volume
    df_feat["ivh_diff_i10_i90"] = i10 - i90

    # Difference in intensity between 25% and 75% volume
    df_feat["ivh_diff_i25_i75"] = i25 - i75

    if not settings.ibsi_compliant:
        # Area under IVH curve
        df_feat["ivh_auc"] = np.trapz(y=df_ivh.nu, x=df_ivh.gamma)

    return df_feat
