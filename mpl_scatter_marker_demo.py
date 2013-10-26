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

print np.__version__
#print plt.__version__

plt.figure(num=None, figsize=(12.5, 10.0))

n=500
np.random.seed(1)
xdata=np.random.uniform(0.0, 1.0, n)
np.random.seed(2)
ydata=np.random.uniform(0.0, 1.0, n)

#plt.xlabel('X')
#plt.ylabel('Y')


nxplot=5
nyplot=5
aspect=1.0

#plt.subplots_adjust(wspace=0.15, hspace=0.15)

markers=['.','*','+','o']


iplot=0

iplot += 1  
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])
plt.scatter(xdata, ydata)

iplot += 1  
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])
plt.scatter(xdata, ydata, color='blue')


iplot += 1  
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])
plt.plot(xdata, ydata, '.')


iplot += 1  
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])
plt.plot(xdata, ydata, marker='.')

iplot += 1  
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])
plt.plot(xdata, ydata, marker='.', lw=0, 
 color='blue', markeredgecolor='blue')


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
    if iy > 1: ms=(iy-1)*5

    if iy == 1: plt.title(marker + ' ' + color)    
    if iy > 1: plt.title(marker + ' ' + 'ms=' + str(ms) + ' ' + color)


    label='data: ' + str(len(xdata))

    #if ms: print 'ms : ', ms

    if iy == 1 and ix < 5: plt.scatter(xdata, ydata, marker=marker, color=color,
     label=label)
    if iy == 1 and ix == 5: plt.scatter(xdata, ydata, marker=marker, 
     color=color, edgecolor=color, label=label)
    
    if iy > 1 and ix < 5 : plt.scatter(xdata, ydata, marker=marker, 
     s=ms, color=color, label=label)
    if iy > 1 and ix == 5: plt.scatter(xdata, ydata, marker=marker, 
     s=ms, color=color, edgecolor=color, label=label)

    #print iplot, ix, iy
    #print

plt.suptitle('matplotlib: plot and scatter marker; \
 markersize and colour tests: ')

# + str(plt.__version__))
plt.savefig('mpl_scatter_marker_demo.png')
plt.show()


