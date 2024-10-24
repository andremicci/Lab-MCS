
#simulazione corda 

import matplotlib.pyplot as plt
from ROOT import * 
import numpy as np
import math
import time





N=100
L=1
x=np.linspace(0,L,N+1)
dx=x[1]-x[0]
dt=0.1
t=0
tmax=10
v_=dx/dt
v=v_*0.7

u=np.zeros(N+1)
u_old=u
u_new=u

A=2
b=7



u_new[1:N-1]=u[1:N-1]+((v/v_)**2)*(u[2:N]+u[0:N-2]-2*u[1:N-1])

fig = plt.figure()
ax = fig.add_subplot()
i=0
while(t<tmax):

    u[0]=A*np.sin(b*t)
    u_new[1:N-1]=u[1:N-1]-u_old[1:N-1]+((v/v_)**2)*(u[2:N]+u[0:N-2]-2*u[1:N-1])
    u[N]=0
    u_old=u
    u=u_new
    ax.plot(t,u[0])
    t=t+dt

plt.show()