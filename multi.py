import numpy as np
import matplotlib.pyplot as p

x=np.array([[1.0,100.0,2.0],[1.0,120.0,3.0],[1.0,150.0,3.0],[1.0,170.0,4.0],[1.0,150.0,4.0],[1.0,190.0,6.0]])
y=np.array([50.0,60.0,80.0,110.0,85.0,150.0])
#y=1000*y
n=6
##x[:,1]=(x[:,1]-np.mean(x[:,1]))
##x[:,2]=(x[:,2]-np.mean(x[:,2]))
##y=(y-np.mean(y))
theta=np.array([0.0,0.0,0.0])
theta=np.transpose(theta)
y=np.transpose(y)
xt=np.transpose(x)

k=0
alpha=0.000000001
while(1):
    a=np.matmul(x,theta)-y
    theta=theta-alpha*np.matmul(xt,a)
    if(abs(np.matmul(a,x)[1])<0.001):
        break
    print theta
    k=k+1
print k
