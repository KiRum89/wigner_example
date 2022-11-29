from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


""" 
plane wave falling onto a slit of width of -a,a
calculate the field intensity using the ray-tracing + wigner function 
"""

def wf(kx,a,x):
    """
    initial wigner function as the slit. Can be found analitically,
    using the wigner function definition
    """

    if 0<=x<=a:
        return 2/kx*( np.sin(kx*2*(a-x)))
    if -a<=x<=0:
        return -2/kx*( np.sin(kx*2*(-x-a)))
    else:
        return 0

kz = 1 # kz is refractive index
a = 20



def trace_back(x,z):
    """
    ray can be found analytically for this simple problem:
    they are just straight lines. Propagate the rays backwards to find where they originated,
    get the value of the wigner function at this point. 
    """
    foo = 0
    dxi = 2*a/1000
    for xi in  np.linspace(-a,a,500):
        kx = (xi-x)/z
        foo+=wf(kx,a,xi)*dxi/z #important: dkx = dxi/z!
    return foo



##plot the field
arr = np.zeros((500,500))
i,j=0,0

zmax = 200

z = np.linspace(0.001,zmax,500)
for x in np.linspace(-2*a,2*a,500):
    arr[i,:]=trace_back(x,z)
    i+=1


plt.imshow(arr)
plt.ylabel('kx*x')
plt.xlabel('kz*z')
