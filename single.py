import numpy as np
import matplotlib.pyplot as p

x=np.array([[1.0,2.0],[1.0,3.0],[1.0,4.0],[1.0,5.0],[1.0,6.0],[1.0,7.0]])
y=np.array([2.0,3.0,4.0,5.0,6.0,7.0])
#y=1000*y
n=6
x[:,1]=(x[:,1]-np.mean(x[:,1]))
y=(y-np.mean(y))
theta=np.array([0.0,0.0])
theta=np.transpose(theta)
y=np.transpose(y)
xt=np.transpose(x)

k=0
alpha=1.0/10000
while(1):
    a=np.matmul(x,theta)-y
    theta=theta-alpha*np.matmul(xt,a)
    if(abs(np.matmul(a,x)[1])<0.0001):
        break
    print theta
    k=k+1
print k
