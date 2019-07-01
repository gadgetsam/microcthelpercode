#Written by Julian A. Davis and Josh Avery
##If you get matlab agg error run:
#
  #sudo yum install python36-tkinter

import tkinter
import matplotlib
import matplotlib.pyplot as mplot
mplot.switch_backend("TkAgg")
plt=mplot
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np
import types
#help(types.CodeType)
import pandas as pd
import os
import glob
from pathlib import Path
import re
import math
import matlab
#matplotlib.get_backend()
#/etc/portage/make.confAdd tc to the system's global USE flags:

#USE="tk"

os.chdir("/home/JADavi/Desktop/microcthelpercode/Porosity Calculations/Done_csv_data")

pathlist = Path('/home/JADavi/Desktop/microcthelpercode/Porosity Calculations').glob('**/*.xlsx')

count = 0
for N in range (1000000, 1000000,100000):
    if N%4 == 0:
        count = count + 1

# filenames
excel_names = ["porosity"+str(count)+'.xlsx']

# read them in
excels = [pd.ExcelFile(name) for name in excel_names]

# turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

# concatenate them..
combined = pd.concat(frames)

# write it out
combined.to_excel("combined.xlsx", header=False, index=False)
#need pyxl
##pip install openpyxl

#------------------Ploting/coloring:



print ("Starting Ploting")
#
# make these smaller to increase the resolution
dx, dy = 0.05, 0.05

# generate 2 2d grids for the x & y bounds
y, x = np.mgrid[slice(0, 1300 + dy, dy), #time
                slice(0, 600 + dx, dx)] #slice

z = np.sin(x)**10\
    + np.cos(10 + y*x) * np.cos(x)

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
cf = ax1.contourf(x[:-1, :-1] + dx/2.,
                  y[:-1, :-1] + dy/2., z, levels=levels,
                  cmap=cmap)
fig.colorbar(cf, ax=ax1)
ax1.set_title('contourf with levels')

# adjust spacing between subplots so `ax1` title and `ax0` tick labels
# don't overlap
fig.tight_layout()

plt.show()

