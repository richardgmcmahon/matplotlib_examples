import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np

im = np.arange(100)
im.shape = 10, 10

# size in inches
fig = plt.figure(1, (5., 5.))

nxcol=5
nycol=5
grid = ImageGrid(fig, 111, # similar to subplot(111)
                nrows_ncols = (nxcol, nycol), # creates 2x2 grid of axes
                axes_pad=0.1, # pad between axes in inch.
                )

for i in range(nxcol*nycol):
    grid[i].imshow(im) # The AxesGrid object work as a list of axes.

plt.show()
