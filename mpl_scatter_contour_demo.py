"""

Test program to try out AstroML scatter_contour


"""

# use native matplotlib or matplotlib.pyplot
#import matplotlib as plt
import matplotlib.pyplot as plt
from astroML.plotting import scatter_contour

import numpy as np

#print 'np.random.get_state(): ', np.random.get_state()

plt.figure(num=None, figsize=(10, 10))


n=10000
np.random.seed(1)
xdata=np.random.normal(0.0, 1.0, n)
np.random.seed(2)
ydata=np.random.normal(0.0, 1.0, n)

iplot=1
plt.subplot(2,2,iplot)

#plt.xlabel('X')
#plt.ylabel('Y')

plt.subplot(2,2,iplot)
plt.title("scatter: '.', s=2, color='red'")
label='data: ' + str(len(xdata))
marker='.'
plt.scatter(xdata, ydata, marker=marker, s=2, color='red', 
  label=label)
plt.legend(loc=2)

plt.xlim(-5.0, 5.0)
plt.ylim(-5.0, 5.0)




# using mplot to get same result as scatter
# ms=1 makes invisible points
iplot = iplot+1
plt.subplot(2,2,iplot)


plt.title("plot: '.', ms=2, color='r'")
label='data: ' + str(len(xdata))
marker='.'
color='red'
plt.plot(xdata, ydata, marker=marker, ms=2, lw=0, color=color, 
  markeredgecolor=color, label=label)
plt.legend(loc=2)

plt.xlim(-5.0, 5.0)
plt.ylim(-5.0, 5.0)


iplot=iplot+1
plt.subplot(2,2,iplot)
threshold=10

# note ax=plt within arguments
plt.title("scatter_contour: '.', markersize=2, color='red'")
label='data: ' + str(len(xdata))
scatter_contour(xdata, ydata, threshold=threshold, log_counts=True, 
                histogram2d_args=dict(bins=40),
                ax=plt,
                plot_args=dict(marker='.', linestyle='none',
                               markersize=2, color='red',
                               markeredgecolor='red',
                               label=label),
                contour_args=dict(cmap=plt.cm.rainbow))

plt.xlim(-5.0, 5.0)
plt.ylim(-5.0, 5.0)

iplot=iplot+1
plt.subplot(2,2,iplot)
threshold=10
plt.title("scatter_contour: 'o', markersize=2, color='blue'")
scatter_contour(xdata, ydata, threshold=threshold, log_counts=True, 
                histogram2d_args=dict(bins=20),
                ax=plt,
                plot_args=dict(marker='o', linestyle='none',
                               markersize=2, color='blue',
                               markeredgecolor='blue'),
                contour_args=dict(cmap=plt.cm.rainbow))

plt.xlim(-5.0, 5.0)
plt.ylim(-5.0, 5.0)


plt.suptitle('matplotlib scatter_contour tests')
plt.savefig('mpl_scatter_contour_demo.png')
plt.show()


   
