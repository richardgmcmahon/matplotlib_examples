import matplotlib.pyplot as plt
import numpy as np

def make_image(inputname,outputname):
    # data = mpimg.imread(inputname)[:,:,0]

    data = np.arange(1,10).reshape((3, 3))

    fig = plt.figure(frameon=False)
    fig.set_size_inches(2, 2)

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    plt.set_cmap('hot')

    ax.imshow(data, aspect = 'normal')
    plt.savefig(outputname, dpi = 200)

make_image(None,'tightimage.png')
