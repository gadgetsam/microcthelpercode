import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from concat_csv import concat_csv
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator





def graph(path):
    print(path)
    data = concat_csv(path)
    print(data.shape)
    print(data[2].max())
    dx, dy = 1, 5

    # generate 2 2d grids for the x & y bounds
    y, x = np.mgrid[slice(0, 1300 + dy, dy),  # slice
                    slice(0, 600+ dx, dx)]  # time
    print(y.shape)
    z = np.zeros([260,1300])
    for row in z.iter
    print(z.shape)

    # x and y are bounds, so z should be the value *inside* those bounds.
    # Therefore, remove the last value from the z array.
    z = z[:-1, :-1]
    levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())

    # pick the desired colormap, sensible levels, and define a normalization
    # instance which takes data values and translates those into levels.
    cmap = plt.get_cmap('PiYG')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

    fig, (ax0, ax1) = plt.subplots(nrows=2)

    im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
    fig.colorbar(im, ax=ax0)
    ax0.set_title('pcolormesh with levels')

    # contours are *point* based plots, so convert our bound into point
    # centers
    cf = ax1.contourf(x[:-1, :-1] + dx / 2.,
                      y[:-1, :-1] + dy / 2., z, levels=levels,
                      cmap=cmap)
    fig.colorbar(cf, ax=ax1)
    ax1.set_title('contourf with levels')

    # adjust spacing between subplots so `ax1` title and `ax0` tick labels
    # don't overlap
    fig.tight_layout()

    plt.show()


if __name__ == "__main__":
    path = "/media/samschickler/1F6D-D692/Porosity"
    graph(path)