import numpy as np
import sympy
import matplotlib.pyplot as plt

# Definimos el método de Runge-Kutta de 4to orden para implementarlo en la resolución
# de un sistema de dos EDO 

def rk4ind(f,g,a,b,h,VI):
    N=int((b-a)/h)
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))

    x[0], y[0] = VI # condiciones iniciales del problema

    for i in range(1,N+1):
        k1x = h*f(x[i-1], y[i-1])
        k1y = h*g(x[i-1], y[i-1])

        k2x = h*f(x[i-1]+ k1x/2.0, y[i-1] + k1y/2.0)
        k2y = h*g(x[i-1]+ k1x/2.0, y[i-1] + k1y/2.0)

        k3x = h*f(x[i-1]+ k2x/2.0, y[i-1] + k2y/2.0)
        k3y = h*g(x[i-1]+ k2x/2.0, y[i-1] + k2y/2.0)

        k4x = h*f(x[i-1]+ k3x, y[i-1] + k3y)
        k4y = h*g(x[i-1]+ k3x, y[i-1] + k3y)

        x[i] = x[i-1] + k1x/6.0 + k2x/3.0 + k3x/3.0 + k4x/6.0
        y[i] = y[i-1] + k1y/6.0 + k2y/3.0 + k3y/3.0 + k4y/6.0
    return x,y



        