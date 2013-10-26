import numpy as np
import matplotlib.pyplot as plt

import plotid

#from pylab import *

# for non-pylab need to prefix the method names

def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 10
x = np.linspace(-3,3,5*n)
y = np.linspace(-3,3,5*n)
X,Y = np.meshgrid(x,y)


# Customising Matplotlib
# see http://matplotlib.org/users/customizing.html

# The figure subplot parameters.  All dimensions are a fraction of the
# figure width or height
#figure.subplot.left    : 0.125  # the left side of the subplots of the figure
#figure.subplot.right   : 0.9    # the right side of the subplots of the figure
#figure.subplot.bottom  : 0.1    # the bottom of the subplots of the figure
#figure.subplot.top     : 0.9    # the top of the subplots of the figure
#figure.subplot.wspace  : 0.2    # the amount of width reserved for blank space between subplots
#figure.subplot.hspace  : 0.2    # the amount of height reserved for white space between subplots

# leave some space to add annotation at the top of the page
plt.rc('figure.subplot', left=0, right=0.98, bottom=0, top=0.95, 
 wspace=0.0, hspace=0.0)

plt.figure(figsize=(10.0, 8.0*1.05))

#plt.subplot(1,21,1)

transform=plt.gcf().transFigure
transform=plt.gca().transAxes


info='Top Title'*5
def toptitle(text):
  """ 
  Add some text to the top of the page 
  It is added as part of the first subplot 
  """
  plt.text(0.5, 1.10, text, transform=plt.gca().transAxes)

noticks=True

plotid.plotid()

nx=4
ny=5
iplot=0
for iy in range (ny):
  for ix in range (nx):
    iplot += 1  
    if noticks: plt.subplot(nx,ny,iplot,frameon=True, xticks=[], yticks=[])
    #subplot(2,2,1)
    
    if iplot == 1: toptitle(info)     
    if iplot == nx*ny: plotid.plotid() 

    plt.text(0.1, 0.9, str(iplot), transform=plt.gca().transAxes)

    plt.imshow(f(X,Y))

plt.savefig('subplot_images_tight.png')

plt.show()

#pylab.imshow(image)
#subplot(2,2,2)
#imshow(image)
#subplot(2,2,3)
#imshow(image)
#subplot(2,2,4)
#imshow(image)


