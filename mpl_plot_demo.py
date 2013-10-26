"""

Test program to show some Matplotlib marker oddities or features

The plot function has a feature that it defaults to
have a black marker edge. This can be modified using 
the parameter markeredgecolor. e.g.

see http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

"""

# use native matplotlib or matplotlib.pyplot
#import matplotlib as plt
import matplotlib.pyplot as plt

import numpy as np

print 'Numpy version: ', np.__version__
#print plt.__version__

plt.figure(num=None, figsize=(10.0, 10.0))

n=500
np.random.seed(1)
xdata=np.random.uniform(0.0, 1.0, n)
np.random.seed(2)
ydata=np.random.uniform(0.0, 1.0, n)

#plt.xlabel('X')
#plt.ylabel('Y')


nxplot=3
nyplot=3
aspect=1.0
iplot=0

#plt.subplots_adjust(wspace=0.15, hspace=0.15)

markers=['.','o']

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.plot(xdata, ydata)

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.plot(xdata, ydata, marker='.')

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.plot(xdata, ydata, '.')


iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.plot(xdata, ydata, 'r.')

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
# mec=markeredgecolor
plt.plot(xdata, ydata, 'r.', mec='r')

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
# mec=markeredgecolor
plt.plot(xdata, ydata, '.', mec='r', c='r')

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
# mec=markeredgecolor
plt.plot(xdata, ydata, '.', mec='r', mfc='r')

iplot = iplot + 1
# This might not work
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)

# mec=markeredgecolor
plt.set_mec=('red')
plt.set_mfc=('red')
plt.plot(xdata, ydata, '.')
plt.set_mec=('red')
plt.set_mfc=('red')

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
# mec=markeredgecolor
plt.plot(xdata, ydata, marker='.', mfc='b', lw=0, mec='b')

plt.suptitle('matplotlib: plot examples showing markeredgecolor issues')

# + str(plt.__version__))
plt.savefig('mpl_plot_demo.png')
plt.show()
