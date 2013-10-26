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
plt.scatter(xdata, ydata)

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.scatter(xdata, ydata, edgecolor='none')

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.scatter(xdata, ydata, marker='.')

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.scatter(xdata, ydata, marker='.', color='red')

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.scatter(xdata, ydata, marker='.', color='red', s=10)

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.scatter(xdata, ydata, marker='.', color='red', s=100)


iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.scatter(xdata, ydata, marker='o')

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.scatter(xdata, ydata, marker='o', color='r')

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect)
plt.scatter(xdata, ydata, marker='o', color='r', edgecolor='r')

plt.suptitle('matplotlib: plot examples showing markeredgecolor issues')

# + str(plt.__version__))
plt.savefig('mpl_scatter_demo.png')
plt.show()
