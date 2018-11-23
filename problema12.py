import matplotlib.pyplot as plt
import funciones12


n = 1.0 # n=a
m = 10000.0 # m=b

# Tamaño

h = 0.01
# Valor Inicial: v(0)=1, w(0)=0

VI = [1,0]

# Constantes del problema

rho=0.5

phi=0.8

I=0.5

# Definimos las dos funciones del problema

def f(v,w):
    return w+v-((v**3)/3)+0.5

def g(v,w):
    return -v+0.5-0.8*w


perro=funciones12.rk4ind(f,g,n,m,h,VI)

print(perro)

plt.plot(perro[0], perro[1])
plt.show()
plt.plot(perro[0],t)

