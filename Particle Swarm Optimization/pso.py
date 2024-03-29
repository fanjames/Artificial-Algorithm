from numpy import array
import numpy as np
from random import random
from math import sin, sqrt, exp, cos, pi
import matplotlib.pyplot as plt

iter_max = 10000
pop_size = 200
dimensions = 2
c1 = 2
c2 = 2
err_crit = 1e-5

class Particle:
    pass

def f6(param):
    '''Schaffer's F6 function'''
    para = param*10
    para = param[0:2]
    num = (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) * \
        (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) - 0.5
    denom = (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1]))) * \
            (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1])))
    f6 =  0.5 - (num/denom)
    errorf6 = 1 - f6
    return f6, errorf6

def nlfun(param):
    '''Nonlinear function'''
    para = param[0:2]
    factor1 = sin(sqrt(para[0]**2 + para[1]**2)) / (sqrt(para[0]**2 + para[1]**2))
    factor2 = exp((cos(2*pi*para[0]) + cos(2*pi*para[1]))/2)
    fun = factor1 + factor2
    error = 3.718282 - fun
    return fun, error

#initialize the particles
particles = []
for i in range(pop_size):
    p = Particle()
    p.params = array([random() for i in range(dimensions)])
    p.fitness = 0.0
    p.v = 0.0
    particles.append(p)

# let the first particle be the global best
gbest = particles[0]
best_fitness = []
while i < iter_max :
    for p in particles:
        fitness,  err = nlfun(p.params)
        if fitness > p.fitness:
            p.fitness = fitness
            p.best = p.params

        if fitness > gbest.fitness:
            gbest = p
        v = p.v + c1 * random() * (p.best - p.params) \
                + c2 * random() * (gbest.params - p.params)
        p.params += v

    i += 1
    if np.abs(err) < err_crit:
        break
    #progress bar. '.' = 10%
    if i % (iter_max/10) == 0:
        print '.',

    best_fitness.append(gbest.fitness)

print '\nParticle Swarm Optimisation\n'
print 'PARAMETERS\n','-'*10
print 'Population size : ', pop_size
print 'Dimensions      : ', dimensions
print 'Error Criterion : ', err_crit
print 'c1              : ', c1
print 'c2              : ', c2
print 'function        :  f6'
print
print 'RESULTS\n', '-'*7
print 'gbest fitness   : ', gbest.fitness
print 'gbest params    : ', gbest.params
print 'iterations      : ', i+1
## Uncomment to print particles
#for p in particles:
#    print 'params: %s, fitness: %s, best: %s' % (p.params, p.fitness, p.best)


plt.figure()
plt.plot(best_fitness)
plt.show()
