"""

Test program to show some Matplotlib marker oddities or features

The plot function has a feature that it defaults to
have a black marker edge. This can be modified using 
the parameter markeredgecolor. e.g.


"""

# use native matplotlib or matplotlib.pyplot
#import matplotlib as plt
import matplotlib.pyplot as plt

import numpy as np

print 'Numpy version: ', np.__version__
#print plt.__version__

plt.figure(num=None, figsize=(12.5, 10.0))

n=500
np.random.seed(1)
xdata=np.random.uniform(0.0, 1.0, n)
np.random.seed(2)
ydata=np.random.uniform(0.0, 1.0, n)

#plt.xlabel('X')
#plt.ylabel('Y')


nxplot=4
nyplot=5
aspect=1.0

#plt.subplots_adjust(wspace=0.15, hspace=0.15)

markers=['.','*','+','o']

iplot=0
for iy in range (1, 5):
  for ix in range (1, 6):
    iplot += 1  
    #print iplot, ix, iy

    plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
     xticks=[], yticks=[])

    color='red'

    # cycle through the markers; where ix=5, change the markeredgecolor
    if ix < 5: marker=markers[ix-1]
    if ix == 5: marker=markers[3]

    # default markersize at iy=0 
    if iy > 1: ms=iy-1

    if iy == 1: plt.title(marker + ' ' + color)    
    if iy > 1: plt.title(marker + ' ' + 'ms=' + str(ms) + ' ' + color)


    label='data: ' + str(len(xdata))

    if iy == 1 and ix < 5: plt.plot(xdata, ydata, marker, color=color,
     label=label)
    if iy == 1 and ix == 5: plt.plot(xdata, ydata, marker, color=color,
     markeredgecolor=color, label=label)

    if iy > 1 and ix < 5 : plt.plot(xdata, ydata, marker, ms=ms, color=color,
     label=label)
    if iy > 1 and ix == 5: plt.plot(xdata, ydata, marker, ms=ms, color=color,
     markeredgecolor=color, label=label)

    plt.legend(loc=2)

    #print iplot, ix, iy
    #print

plt.suptitle('matplotlib marker, markersize and colour tests: ')
# + str(plt.__version__))
plt.savefig('mpl_plot_marker_demo.png')
plt.show()


