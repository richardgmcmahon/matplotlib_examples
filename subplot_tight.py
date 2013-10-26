from pylab import *

N=[4, 8, 16, 64]

figure(frameon=False)

for i, n in enumerate(N):
  subplot(2,2,i+1)
  stem(arange(n), hanning(n))
  legend(['N=%d' % n])

savefig('subplot_tight.png', dpi = 200)
show()
