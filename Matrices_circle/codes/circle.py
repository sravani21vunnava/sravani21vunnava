import math
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

def line_gen(A,B):
    len =10
    dim = A.shape[0] 
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
      temp1 = A + lam_1[i]*(B-A)
      x_AB[:,i]= temp1.T
    return x_AB
#Given Points
A = np.array(([1,-2]))
B = np.array(([3,0]))
W = np.array(([0,0]))
O = np.block([[-5,2],[2,-5],[5,-2],[-2,5]])
#Y = np.arry(([]))
m = np.array(([1,0]))
#Finding Center
A_t = 2*A.T
B_t = 2*B.T
m_t = m.T
i = -np.linalg.norm(A)**2
j = -np.linalg.norm(B)**2
k = -m@B
S = np.block([[A_t,1],[B_t,1],[m_t,0]])

#S = np.array(([At,1],[Bt,1],[mt,0]))

T = np.block([i,j,k])
P = LA.solve(S,T)
print(P)
C = np.array(([-P[0],-P[1]]))
print(C)
r = np.linalg.norm(C-A)

#Verification
for i in O:
    if(np.linalg.norm(C-i) == r):
        print(i,end = "")
        print(" lies on the circle")
        Y = np.array(([i]))
#Circle generation and plotting
x_circ = circ_gen(C,r)
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')	
x_BW = line_gen(B,W)                                                                    
plt.plot(x_BW[0,:],x_BW[1,:],label='$Tangent$')
tri_coords = np.vstack((A,B,Y,C,W)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','Y','C','W']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig('/sdcard/sravani21vunnava/trunk/Matrices_circle/cir.pdf')
