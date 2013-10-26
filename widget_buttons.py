# from matplotlib examples

# rgm trying to add image support so that one could look through 
# cutouts in a directory


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

freqs = np.arange(2, 20, 3)

image=True

ax = plt.subplot(111)
plt.subplots_adjust(bottom=0.2)

t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)

if not image:
  l, = plt.plot(t, s, lw=2)
  help(l)

min0 = 0
max0 = 25000
nx, ny = 10, 10
im = max0 * np.random.random((nx,ny))
if image:
  l=plt.imshow(im)
  print 'shape: ', im.shape
  print 'len: ',len(im)
  print 'min, max: ', min(im.flat), max(im.flat)

  help(l)

class Index:
    ind = 0
    def next(self, event):
        min0 = 0
        max0 = 25000

        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        max0=max0*2
        im = max0 * np.random.random((nx,ny))
        if not image:
          l.set_ydata(ydata)
          plt.draw()
        if image:
          print im.shape
          print len(im)
          print min(im.flat), max(im.flat)
          ax.imshow(im, cmap=plt.cm.gray)

    def prev(self, event):
        min0 = 0
        max0 = 25000

        self.ind -= 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        max0=max0*2
        im = max0 * np.random.random((ny*4,ny*4))
        if not image:
          l.set_ydata(ydata)
          plt.draw()
        if image:
          print im.shape
          print len(im)
          print min(im.flat), max(im.flat)
          ax.imshow(im)

icheck=0
icheck=icheck+1
raw_input(str(icheck)+': Type any key to continue> ')

callback = Index()

raw_input('Type any key to continue> ')

axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])

raw_input('Type any key to continue> ')

bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

raw_input('Type any key to continue> ')

plt.show()

