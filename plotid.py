"""

add timestamp and username

add some info text to border in normalised screen/figure cordinates


uses mpl.text 

need to compare with mpl.annotate

"""

import matplotlib.pyplot as plt

def plotid(xpos=0.70, ypos=0.02):

  import os
  import time
  import datetime
  import getpass

  now = time.localtime(time.time())
  timestamp = time.strftime("%Y-%m-%dT%H:%M:%S",now)

  #username=os.environ['USER']
  username = getpass.getuser()

  # generate text string using obscure format
  text = '{}: {}'.format(username, timestamp)


  # choose the cordinate system

  # axes one
  #transform = plt.gca().transAxes

  # figure one
  transform=plt.gcf().transFigure

  plt.text(xpos, ypos,
    text,
    transform=transform,
    rotation=0,
    size='small',
    weight='ultralight',
    horizontalalignment='left', verticalalignment='center')






