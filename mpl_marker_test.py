"""

Test program to show some Matplotlib problems


"""

# use native matplotlib or matplotlib.pyplot
#import matplotlib as plt
import matplotlib.pyplot as plt

import numpy as np

plt.figure(num=None, figsize=(12.5, 10.0))

np.random.seed(1)
n=500
xdata=np.random.uniform(0.0, 1.0, n)
ydata=np.random.uniform(0.0, 1.0, n)

#plt.xlabel('X')
#plt.ylabel('Y')


nxplot=4
nyplot=5
aspect=1.0

#plt.subplots_adjust(wspace=0.15, hspace=0.15)

iplot=1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("'.', color='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, '.', color='red',
 label=label)
plt.legend(loc=2)
#ax.set_xticks([])
#ax.set_yticks([])


iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect, 
 xticks=[], yticks=[])

plt.title("'*', color='red'")
label='data: ' + str(len(xdata))
marker='*'
plt.plot(xdata, ydata, marker, c='red', 
  label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("'+', color='red'")
label='data: ' + str(len(xdata))
marker='+'
plt.plot(xdata, ydata, marker, c='r', 
  label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("'o', color='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, 'o', c='r', 
  label=label)
plt.legend(loc=2)



iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("'o', color='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, 'o', color='red',  
  markerfacecolor='red', markeredgecolor='red', 
  label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("'.', ms=1, c='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, '.', ms=1, c='r',
 label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("'*', ms=1, c='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, '*', ms=1, c='red', 
  label=label)
plt.legend(loc=2)


iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("'+', ms=1, c='red'")
label='data: ' + str(len(xdata))
marker='+'
plt.plot(xdata, ydata, marker, ms=1, c='r', 
  label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("'o', ms=1, c='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, 'o', ms=1, c='r', 
  label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])


plt.title("'o', ms=1, color='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, 'o', ms=1, color='red',  
  markerfacecolor='red', markeredgecolor='red', 
  label=label)
plt.legend(loc=2)



iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("'.', ms=2, c='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, '.', ms=2, c='r', 
  label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect, 
 xticks=[], yticks=[])

plt.title("'*', ms=2, c='r'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, '*', ms=2, c='r', 
  label=label)
plt.legend(loc=2)


iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("'+', ms=2, c='r'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, '+', ms=2, c='r', 
  label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect, 
 xticks=[], yticks=[])

plt.title("'o', ms=2, c='r'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, 'o', ms=2, c='r', 
  label=label)
plt.legend(loc=2)


iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])
plt.title("'o', ms=2, color='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, 'o', ms=2, color='red',  
  markerfacecolor='red', markeredgecolor='red', 
  label=label)
plt.legend(loc=2)



iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title(".', ms=3, color='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, '.', ms=3, color='red', 
  label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("*', ms=3, color='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, '*', ms=3, color='red', 
  label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])

plt.title("+', ms=3, color='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, '+', ms=3, color='red', 
  label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect, 
 xticks=[], yticks=[])

plt.title("o', ms=3, color='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, 'o', ms=3, color='red', 
  label=label)
plt.legend(loc=2)

iplot=iplot+1
plt.subplot(nxplot,nyplot,iplot, aspect=aspect,
 xticks=[], yticks=[])
plt.title("'o', ms=3, color='red'")
label='data: ' + str(len(xdata))
plt.plot(xdata, ydata, 'o', ms=3, color='red',  
  markerfacecolor='red', markeredgecolor='red', 
  label=label)
plt.legend(loc=2)



plt.suptitle('matplotlib marker, markersize and colour tests')
plt.savefig('matplotlib_markersize_tests.png')
plt.show()


   
