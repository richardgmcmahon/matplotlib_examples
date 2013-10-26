from pylab import *

f1.figure(1)
f2.figure(2)

f1.plot([1,2,3])
f2.plot([10, 20, 30])
f1.plot([4, 5, 6])
f2.plot([40, 50, 60])

f1.savefig(1,'fig1.png', dpi = 200)
f2.savefig(2,'fig2.png', dpi = 200)

show()
