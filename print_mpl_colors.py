# Python 3 print function
from __future__ import print_function


import matplotlib.pyplot as plt

def print_colors():

  import matplotlib.pyplot as plt

  print('lines.color: ', plt.rcParams['lines.color'])
  print('patch.facecolor: ', plt.rcParams['patch.facecolor'])
  print('patch.edgecolor: ', plt.rcParams['patch.edgecolor'])
  print('text.color: ', plt.rcParams['text.color'])

  print('axes.facecolor: ', plt.rcParams['axes.facecolor'])
  print('axes.edgecolor: ', plt.rcParams['axes.edgecolor'])
  print('axes.labelcolor: ', plt.rcParams['axes.labelcolor'])

  print('xtick.color: ', plt.rcParams['xtick.color'])
  print('ytick.color: ', plt.rcParams['ytick.color'])
  print('grid.color: ', plt.rcParams['grid.color'])

  print('figure.edgecolor: ', plt.rcParams['figure.edgecolor'])
  print('figure.facecolor: ', plt.rcParams['figure.facecolor'])

  print('savefig.edgecolor: ', plt.rcParams['savefig.edgecolor'])
  print('savefig.facecolor: ', plt.rcParams['savefig.facecolor'])

print_colors()

