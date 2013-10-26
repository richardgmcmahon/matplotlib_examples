from pylab import *

N=[4, 8, 16, 64]

for i, n in enumerate(N):
  subplot(2,2,i+1)
  stem(arange(n), hanning(n))
  legend(['N=%d' % n])

show()
