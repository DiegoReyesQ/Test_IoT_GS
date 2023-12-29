# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 01:22:09 2023

@author: Diego
"""

#Librerías utilizadas

import numpy as np
import matplotlib.pyplot as plt
from Adafruit_IO import Client
import time

#%% Definición de funciones y parámetros

aio = Client('DiegoRQ','aio_OGhb79q3ujMCBfDWBz3iLJLZW1el')
tiempo = 2      #Tiempo de muestreo (seg)
muestra = 100  #Cantidad de muestras

def sen(x):
    return np.sin(x)
    pass

def cos(x):
    return np.cos(x)
    pass

if __name__=='__main__':
    x = np.linspace(0,10,muestra)    #Valores de x y 
    y = sen(x)  #Matriz de valores de se(x)
    #print(y)
    y2 = cos(x)
    #print(y2)

#%% Gráfica de referencia con Matplotlib
    
    plt.plot(x,y,color="red")
    plt.plot(x,y2,color="blue")
    plt.title("Función seno y coseno")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

#%% Envío de valores de función seno y coseno
    
   for i in range(muestra):
       aio.send('seno',y[i])     #Envío de datos al feed de la función seno
       data = aio.receive('seno')
       print('Received sin() value: {0}'.format(data.value))
       time.sleep(tiempo)
       aio.send('coseno',y2[i])  #Envío de datos al feed de la función coseno
       data = aio.receive('coseno')
       print('Received cos() value: {0}'.format(data.value))
       time.sleep(tiempo)

