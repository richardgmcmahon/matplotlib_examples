import sys

import matplotlib.pylab as plt
from matplotlib.widgets import Button

fig = plt.figure()

def callback(event):
    print "clicked:", event
    sys.stdout.flush()

ax1 = plt.axes([0.2, 0.1, 0.1, 0.075])
ax2 = plt.axes([0.4, 0.1, 0.1, 0.075])
ax3 = plt.axes([0.6, 0.1, 0.1, 0.075])

b1 = Button(ax1, 'Button 1')
b1.on_clicked(callback)

b2 = Button(ax2, 'Button 2')
b2.on_clicked(callback)

b3 = Button(ax3, 'Button 3')
b3.on_clicked(callback)

plt.show()
