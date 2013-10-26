# from stackoverflow
# http://stackoverflow.com/questions/7614949/interactive-image-plotting-with-matplotlib

from pylab import * 
import sys
from numpy import *
from matplotlib import pyplot

class Test:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __call__(self,event):
    if event.inaxes:
      print("Inside drawing area!")
      print("x: ", event.x)
      print("y: ", event.y)
    else:
      print("Outside drawing area!")

if __name__ == '__main__':     
  x = range(10)
  y = range(10)      
  fig = pyplot.figure("Test Interactive")
  pyplot.scatter(x,y)
  test = Test(x,y)
  connect('button_press_event',test)     
  pyplot.show()
