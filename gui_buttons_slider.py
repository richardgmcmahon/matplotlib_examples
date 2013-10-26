"""
    %prog [options]

Take the query on standard input, or via the -q parameter.  Write the results
on standard output.

username/password are by default gotten from ~/.netrc, but can be sent as
options
"""

# slider example from stackoverflow
# http://stackoverflow.com/questions/5611805/using-matplotlib-slider-widget-to-change-clim-in-image

# add comment option as a button with text entry in console

# also a help button that write out help to the console

# same text as -h -help

import sys

import matplotlib.pyplot as plt
import numpy as np


from matplotlib.widgets import Button, CheckButtons, Cursor, \
  RadioButtons, Slider


#def main():



from optparse import OptionParser
parser=OptionParser(__doc__)
parser.add_option("-p","--path",default=None, help="Path to images")

options,args = parser.parse_args(sys.argv[1:])

#fig=plt.figure(figsize=(8.0, 8.0))
#fig.set_size_inches((10.0,10.0))

fig, ax = plt.subplots(figsize=(12,8))
fig.subplots_adjust(bottom=0.20, top=0.80, left=0.1, right=0.5)

# add some annontation: e.g. figure name

fig.text(0.1, 0.85, 'fig.text: Hello World', transform=fig.transFigure)
ax.text(0.5, 0.5, 'ax.text', transform=ax.transAxes)



t = np.linspace(0, 10, 1000)
line, = plt.plot(t, np.sin(t), lw=2)

print 'Hello World'
text=(0.5, 0.5, 'ax.text 0.5')
plt.text=(0.5, 0.5, 'ax.text 0.5')
ax.text=(0.5, 0.5, 'ax.text 0.5')
fig.text=(0.5, 0.5, 'fig.text 0.5')
line.text=(0.5, 0.5, 'line.text 0.5')

class Index:
    dt = 1
    def next(self, event):
        print "You pushed 'next'"
        self.dt += 1
        print 'counter: ', self.dt
        line.set_ydata(np.sin(t + self.dt))
        fig.canvas.draw()
        fig.text=(0.5, 0.5, 'fig.text 0.5')
        line.text=(0.5, 0.5, 'line.text 0.5')

    def prev(self, event):
        print "You pushed 'back'"
        self.dt -= 1
        print 'counter: ', self.dt
        line.set_ydata(np.sin(t + self.dt))
        fig.canvas.draw()

    def exit(self, event):
        print "You pushed 'Exit'"
        print "Results are saved in this file"
        plt.close('all')

    def invert(self, event):
        print "You pushed 'Invert'"
        print "Inverting colormap"

    def reset(self, event):
        print "You pushed 'Reset'"
        print "Reset image display"

    def submit(self, event):
        print "You pushed 'Submit and show next'"
        print "Saved to log file"

    def mark(self, event):
        print "You pushed 'Mark'"
        print "Mark for return or resumption"



axcolor = 'lightgoldenrodyellow'
axmin = fig.add_axes([0.10, 0.05, 0.45, 0.03], axisbg=axcolor)
axmax = fig.add_axes([0.10, 0.10, 0.45, 0.03], axisbg=axcolor)

min0 = 0
max0 = 25000
smin = Slider(axmin, 'Min', 0, 30000, valinit=min0)
smax = Slider(axmax, 'Max', 0, 30000, valinit=max0)

def slider_update(val):
    im1.set_clim([smin.val,smax.val])
    fig.canvas.draw()
smin.on_changed(slider_update)
smax.on_changed(slider_update)

callback = Index()

axprev = plt.axes([0.70, 0.80, 0.1, 0.05])
axnext = plt.axes([0.80, 0.80, 0.1, 0.05])
axexit = plt.axes([0.85, 0.05, 0.1, 0.05])

axinvert = plt.axes([0.70, 0.91, 0.1, 0.05])
axreset = plt.axes([0.85, 0.91, 0.1, 0.05])

axsubmit = plt.axes([0.70, 0.20, 0.25, 0.05])
axmark = plt.axes([0.80, 0.12, 0.15, 0.05])

bnext = Button(axnext, '>', color='green', hovercolor='green')
bnext.on_clicked(callback.next)

bprev = Button(axprev, '<', color='orange', hovercolor='orange')
bprev.on_clicked(callback.prev)

bexit = Button(axexit, 'Exit', color='red', hovercolor='red')
bexit.on_clicked(callback.exit)

binvert = Button(axinvert, 'Invert')
binvert.on_clicked(callback.invert)

breset = Button(axreset, 'Reset')
breset.on_clicked(callback.reset)

bsubmit = Button(axsubmit, 'Submit and show next', 
  color='green', hovercolor='green')
bsubmit.on_clicked(callback.submit)

bmark = Button(axmark, 'Mark for return', 
  color='orange', hovercolor='orange')
bmark.on_clicked(callback.mark)


axcolor = 'lightgoldenrodyellow'
rb1_axes = plt.axes([0.70, 0.62, 0.10, 0.15], axisbg=axcolor)
radio1 = RadioButtons(rb1_axes, ('A', 'B', 'C'))
def rb_1(label):
  print 'radio button 1'  

radio1.on_clicked(rb_1)


rax = plt.axes([0.70, 0.3, 0.2, 0.25])
labels=['Type 1','Type 2', 'Type 4', 'Other']
check = CheckButtons(rax, (labels[0], labels[1], labels[2], labels[3]), 
 (False, False, False, False))

def func(label):
    if label == labels[0]: check_text=labels[0]
    elif label == labels[1]: check_text=labels[1]
    elif label == labels[2]: check_text=labels[2]
    elif label == labels[3]: check_text=labels[3]
    print 'checked: ', check_text
check.on_clicked(func)


ax.text=(0.9, 0.9, 'ax.text 0.5')
fig.text=(0.9, 0.9, 'fig.text 0.5')


plt.show()


#if __name__=='__main__':
