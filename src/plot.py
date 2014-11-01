foo = open("fre",'r').read().split('\n')[:-1]
fre = [float(x) for x in foo]
import pylab as pl
pl.plot(fre)
