"""
Atractor de Rösler:
x'=-y-z
y'=x+Ay
z'=B+z(x-c)
Donde:
A=1/4 \qquad A=1/4
B=1 \qquad B=1
C=5.5 \qquad C<14
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import funciones

n = 0.0
m = 10000.0
# Tamaño
h = 0.01
# Valor Inicial: y(0.0) = 1.0
VI = (1,0,0) #(x,y,y')

A=1/4
B=1
C=5.5

def f(x,y,z):
    global A,B,C
    return -y-z

def g(x,y,z):
    global A,B,C
    return x+A*y

def e(x,y,z):
    global A,B,C
    return B+z*(x-C)

#rk4(funcion,x[inicia],x[final],paso,valores iniciales,orden de la ED)
num=funciones.rk43ind(f,g,e,n,m,h,VI)


ax = plt.axes(projection='3d')
ax.plot3D(num[0], num[1], num[2],label='A=1/4,B=1,C=5.5')
plt.legend(loc=1)
plt.title("Atractor de Rösler 1 ")
plt.ylabel('y')
plt.xlabel('x')
ax.set_zlabel('y´')
plt.show()

A=1/4
B=1
C=5.5

num=funciones.rk43ind(f,g,e,n,m,h,VI)


ax = plt.axes(projection='3d')
ax.plot3D(num[0], num[1], num[2],label='A=1/4,B=1,C=5.5')
plt.legend(loc=1)
plt.title("Atractor de Rösler 2 ")
plt.ylabel('y')
plt.xlabel('x')
ax.set_zlabel('y´')
plt.show()