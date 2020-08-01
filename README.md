# EcuacionesDiferencialesII

Problema resuelto numéricamente del curso de Ecuaciones Diferenciales II usando el método de Runge-Kutta de 4to orden (problema12.py).

Es un sistema de ecuaciones diferenciales que modela el comportamiento de las neuronas, 
el programa muestra la gráfica del espacio fase. Las ecuaciones son las siguientes:

<img src="https://render.githubusercontent.com/render/math?math=v' = v %2B w - \frac{v^{3}}{3} %2B I_{ext}">
<img src="https://render.githubusercontent.com/render/math?math=w' = -v %2B a - bw">

Resolvemos el sistema con las condiciones:

<img src="https://render.githubusercontent.com/render/math?math=I_{ext} = 0.5, a = 0.7, b = 0.8">

También graficamos el Atractor de Rössler usando el mismo método numérico.
