import numpy as np
import matplotlib.pyplot as p

x=np.array([[1,100,2],[1,120,3],[1,150,3],[1,170,4],[1,150,4],[1,190,6]])
y=np.array([50,60,80,110,85,150])
#y=1000*y
n=6
theta=np.array([0,0,0])

k=0
alpha=1.0/6000

x[:,1]=x[:,1]-np.full((1,6),np.mean(x[:,1]))
x[:,0]=10*x[:,0]

x[:,2]=10*x[:,2]

print x
print y
print theta
while(1):
    a=np.matmul(x,theta)-y
    a=np.transpose(a)
    theta=theta-alpha*np.matmul(a,x)
    if(abs(np.matmul(a,x)[1])<0.01):
        break
    print theta
    k=k+1
print k
