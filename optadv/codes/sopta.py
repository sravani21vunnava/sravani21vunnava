import numpy as np
import matplotlib.pyplot as plt
import cvxpy  as cp

import sys, os
sys.path.insert(0,'/sdcard/Download//chinna/python/CoordGeo')

#if using termux
import subprocess
import shlex
#Defining f(x)
def f(x,V):
 return 2*x**2 + 4*V/x
V = 8
label_str = "$Surface area$"

#For minima using gradient ascent
cur_x = 0.1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 4*x - 4*V/(x**2)            

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x -= alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

min_val = f(cur_x,V)
print("Minimum value of f(x) is ", min_val, "at","x =",cur_x)

#Plotting f(x)
x=np.linspace(0.1,5,100)
y=f(x,V)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.4f},{min_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
plt.savefig("/sdcard/sravani21vunnava/trunk/optadv/opt.pdf")
