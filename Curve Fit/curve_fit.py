# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import curve_fit, leastsq
from numpy import exp, sin, pi
import matplotlib.pyplot as plt
import h5py
from pylab import *
from multiprocessing import Pool
from time import clock
from function import *

mpl.rcParams['font.sans-serif'] = 'KaiTi'
mpl.rcParams['axes.unicode_minus'] = False

def rms(data):
    N = data.shape[0]
    m = np.sqrt(sum(data**2)/N)
    return m


def gen_func(t, params):
    res = np.zeros(t.size)
    for i in range(params.shape[0]):
        a = params[i, 0]
        b = params[i, 1]
        c = params[i, 2]
        d = params[i, 3]
        res += a*exp(-b*t)*sin(2*pi*c*t+d)
##    plt.figure()
##    plt.plot(t, res)
##    plt.show()
    return res

def example(t, params):
    (amp, alpha, freq, theta) = params
    return amp*exp(-alpha*t)*sin(2*pi*freq*t+theta)


f = h5py.File("LOEC2.h5")
group = f['group42']
delta = group['delta'].value
time = group['time'].value
plt.figure(10)
plt.plot(time, delta, label=u'原始曲线')
delta = delta-delta[0]
index = np.where(abs(time-0.5)<0.000001)[0][0]+1
time = time[index:]-0.5
delta = delta[index:]
plt.plot(time, delta, label=u'处理后的曲线')
plt.xlabel('$t(s)$'); plt.ylabel('$\delta(rad)$')
plt.grid()
plt.legend()
plt.savefig('10.jpeg')


p = [0.4, 0.5, 2, 3.6,
     0.5, 0.2, 3, 1.9,
     0.3, 0.5, 3.4, 2.3,
     0.3, 0.5, 2.3, 1.3,
     0.2, 0.4, 2.5, 2.1,
     0.6, 0.7, 2.1, 2.9,
     0.3, 0.8, 2.4, 2.5,
     0.4, 0.3, 2.7, 2.8,
     0.1, 0.4, 2.4, 2.5,
     0.2, 0.1, 2.1, 2.1,
     0.5, 0.4, 2.3, 2.9,
     0.3, 0.9, 2.7, 2.0]
p0 = []
##n = 7
residual = [residual1, residual2, residual3, residual4, residual5, residual6, residual7,
            residual8, residual9, residual10, residual11]

time = np.arange(0, 10, 0.002)
params = [[2, 2, 2, 4],
          [1.4, 1.5, 1.6, 2.1],
          [1.7, 1.1, 2.6, 1.1],
          [1.1, 1.9, 1.2, 2.8],
          [1.4, 1.0, 1.9, 2.3]]
delta = 0
for i in range(5):
    delta += example(time, params[i])

handler = np.arange(0, len(time), 50)
time_change = time[handler]
delta_change = delta[handler]

fit_curve = []
def main(k):
    for i in range(k+1):
        p0 = p[0:4*(i+1)]
    popt, pcov = leastsq(residual[k], p0, args=(delta_change, time_change), maxfev=10000000)
    pp = np.zeros((popt.shape[0]/4, 4))

    for i in xrange(popt.shape[0]/4):
        pp[i] = popt[(4*i):(4*i+4)]
        
    for i in range(pp.shape[0]):
        print ('Amp%d = %f, Alpha%d = %f, Freq%d = %f, Theta%d = %f' %
               (i+1, pp[i, 0], i+1, pp[i, 1], i+1, pp[i, 2], i+1, pp[i, 3]))
    fit_model = gen_func(time, pp)
    SNR = 20*np.log10(rms(delta)/rms(abs(delta-fit_model)))
    print (u'Model Order = %d, SNR = %f dB, 百分比误差 = %f%%' %
           (k+1, SNR, abs(sum(delta-fit_model)/sum(delta-delta[0])*100)))
    print 
    plt.figure(k)
    plt.subplot(211)
    plt.plot(time, delta, 'r', lw=3, label=u'原曲线')
    plt.plot(time, fit_model, 'k--', lw=2, label=u'拟合曲线')
    plt.xlabel('$t(s)$'); plt.ylabel('$\delta(rad)$')
    plt.legend()
    plt.grid()
    plt.title(u"%d阶拟合曲线" % (k+1))
    plt.subplot(212)
    plt.plot(time, delta-fit_model)
    fit_curve.append(fit_model)
    plt.xlabel('$t(s)$'); plt.ylabel('$error(rad)$')
    plt.grid()
    plt.savefig('%d.jpeg' % k)

##pool1 = Pool(1)
##pool2 = Pool(2)
##pool_outputs = pool1.map(main, [1])


for i in range(7):
    start = clock()
    main(i)
    end = clock()
##    print "Elapsed time >%f s" % (end-start)
##    print
    
fig = plt.figure(100)
ax = fig.add_subplot(111)
ax.plot(time, delta)
for i in range(7):
    ax.plot(time, fit_curve[i])
plt.savefig('100.jpeg')

##plt.show()

