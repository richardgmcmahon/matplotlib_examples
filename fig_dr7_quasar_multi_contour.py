"""
SDSS DR7 Quasars
----------------
This example shows how to fetch the SDSS quasar photometric data, and to
plot the relationship between redshift and color.
"""


# Author: Jake VanderPlas <vanderplas@astro.washington.edu>
# License: BSD
#   The figure produced by this code is published in the textbook
#   "Statistics, Data Mining, and Machine Learning in Astronomy" (2013)
#   For more information, see http://astroML.github.com


# Modified by Richard McMahon to plot stacked colours

from matplotlib import pyplot as plt

from astroML.datasets import fetch_dr7_quasar
from astroML.plotting import scatter_contour

#------------------------------------------------------------
# Fetch the quasar data
data = fetch_dr7_quasar()

# select the first 10000 points
data = data[:10000]

u = data['mag_u']
g = data['mag_g']
r = data['mag_r']
i = data['mag_i']
z = data['mag_z']
redshift = data['redshift']

#------------------------------------------------------------
# Plot the quasar data

plt.figure(num=None, figsize=(10.0, 10.0))
nxplot=4
nyplot=1
iplot=0

plt.subplots_adjust(hspace=0.0)


iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot)
xdata=redshift
ydata= i - z
label='data: ' + str(len(xdata))
threshold=5
scatter_contour(xdata, ydata, threshold=threshold, log_counts=True, 
                histogram2d_args=dict(bins=225),
                ax=plt,
                plot_args=dict(marker='.', linestyle='none',
                               markersize=2, color='red',
                               markeredgecolor='red',
                               label=label),
                contour_args=dict(cmap=plt.cm.Reds))

plt.xlim(0.0, 6.0)
plt.ylim(-1.0, 2.0)
plt.ylabel('i - z')


iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot)
plt.plot(redshift, r - i, 
 marker='.', markersize=4, linestyle='none', color='orange',
 markeredgecolor='orange')
plt.ylim(-1.0, 2.0)
plt.ylabel('r - i')

iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot)
plt.plot(redshift, g - r, 
 marker='.', markersize=4, linestyle='none', color='green',
 markeredgecolor='green')
plt.ylim(-1.0, 4.0)
plt.ylabel('g - r')


iplot = iplot + 1
plt.subplot(nxplot,nyplot,iplot)
plt.plot(redshift, u - g, 
 marker='.', markersize=4, linestyle='none', color='blue',
 markeredgecolor='blue')
plt.ylim(-1.0, 4.0)
plt.ylabel('u - g')

#plt.set_xlabel='Redshift'
#plt.set_ylabel='u - g'


plt.suptitle('DR7QSO redshift -v- colour')

plt.savefig('fig_dr7_quasar_multi.png')
plt.show()

