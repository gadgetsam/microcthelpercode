from scipy.interpolate import splrep, sproot, splev

class MultiplePeaks(Exception): pass
class NoPeaksFound(Exception): pass

def fwhm_calc(df):
    """
    Determine full-with-half-maximum of a peaked set of points, x and y.

    Assumes that there is only one peak present in the datasset.  The function
    uses a spline interpolation of order k.
    """

    half_max = df.fiber_density.max()/2.0
    print(df.loc[df['fiber_density']<half_max+5 and df['fiber_density']>half_max-5].head(100))