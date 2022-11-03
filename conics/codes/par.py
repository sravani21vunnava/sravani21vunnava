import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(-12,12,400)
y = np.linspace(-12,12,400)
x,y = np.meshgrid(x,y)
def axes():
	plt.axhline(0,alpha=.1)
	plt.axvline(0,alpha=.1)
axes()
plt.contour(x,y,(y**2 - 16*x),[1],colors='k')

def line_gen(A,B):
   len =10
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB
f = 0
p = 2
u = np.array(([-8,0]))
q = np.array(([0,p]))
m = np.array(([1,-2]))
v1 = np.array(([0,0]))
v2 = np.array(([0,1]))
V = np.block([[v1],[v2]])
w1=m@V@m
w2=V@q+u
w3=q@V@q+2*u@q+f
w4=-m@w2

w5=(w4)**2-w3*w1
ww1=np.sqrt(w5)
u1=(w4+ww1)/w1
u2=(w4-ww1)/w1
'''
u1 = (p+4)/2 + np.sqrt(2*p+4)
u2 = (p+4)/2 - np.sqrt(2*p+4)
'''
A = q + u1*m
B = q + u2*m
M = (A+B)/2
#print(A,B)

h = M[0]
k = M[1]
print(h,k) 
x_AB = line_gen(A,B)
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

tri_coords = np.vstack((A,B,M)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','M']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.xlabel('$x_axis$')
plt.ylabel('$y_axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.title('Parabola')

plt.savefig('/sdcard/sravani21vunnava/trunk/conics/par.pdf')
