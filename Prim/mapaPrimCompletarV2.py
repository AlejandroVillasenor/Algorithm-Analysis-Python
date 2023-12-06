# -*- coding: utf-8 -*-
"""
Tarea 6. Algoritmo de Prim
"""
import cv2
import numpy as np
import random as rd #Para generar numeros aleatorios
#---- Funciones ----
#Funcion para calcular el peso con Pitagoras
def peso(v1,v2):
    return np.sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)
#Funcion para dibujar las lineas del MST
def dibujar_linea_mst(v1, v2, map):
    #Desenpaquetamos los vertices
    x1, y1 = v1[1], v1[0]
    x2, y2 = v2[1], v2[0]
    #Dibujamos la linea
    cv2.line(map, (x1, y1), (x2, y2), (0, 0, 255), 2)#img, punto1, punto2, color, grosor
# Función para dibujar una línea entre dos puntos color verde
def dibujar_linea(v1, v2, th2):
    #Desenpaquetamos los vertices
    x1, y1 = v1[1], v1[0]
    x2, y2 = v2[1], v2[0]
    #Obtenemos el peso de la arista que dictamina el numero de puntos medios
    pesoAc=peso(v1,v2)
    if pesoAc<=100:
        num_puntos=7
    elif pesoAc<=250:
        num_puntos=14
    else:
        num_puntos=18
    # Lista de puntos medios
    puntos_medios = []
    #Bandera para validar la linea a dibujar
    is_valid_line = True
    #  Iteramos sobre el número de puntos medios
    for i in range(num_puntos):
        #Factor de interpolacion lineal
        razon = i / num_puntos #Obtenemos la razón para interpolar los puntos medios
        #Calculamos las coordenadas de los puntos medios
        x = int(x1 + (x2 - x1) * razon)
        y = int(y1 + (y2 - y1) * razon)#Se hace en int para trabajar con enteros
        #Agregamos los puntos medios a la lista
        puntos_medios.append((x, y))
    # Iteramos sobre los puntos medios
    for point in puntos_medios:
        #Comprobamos si el punto medio es un valor negro
        if np.all(th2[point[1], point[0]] == 0):#Es all para comprobar que todo lo que conforma en nuestro vetice es negro (y,x)
            is_valid_line = False
            break#Si hay un pixel negro, invalidamos el trazo
        else:
            is_valid_line = True 
    # Si la línea es válida, la dibujamos
    if is_valid_line:
        cv2.line(th2, (x1, y1), (x2, y2), (0, 255, 0), 1) 
        #La agregamos en las listas correspondientes
        aristas.append((v1, v2))
        pesos.append(pesoAc)
#---- Configuracion del mapa ----
nombreMapa="3"
#para cargar el mapa
mapa=cv2.imread('mapa'+nombreMapa+'.png')
#Para mostrar el mapa
cv2.imshow('mapa'+nombreMapa, mapa)
# Para cargar la lista de indices
vertices=np.load("verticeMapa"+nombreMapa+".npy")
#Obtenemos el numero de vertices
num_vertices = len(vertices)
#Lista de pesos
pesos=[]
#Lista de aristas
aristas=[]
#pasamos la imagen a escala de grises
gray = cv2.cvtColor(mapa,cv2.COLOR_BGR2GRAY)
#muestro la imagen en escala de grises
cv2.imshow('mapa-Escala de grises',gray)
#obtengo un binarizacion en blanco de todos lo pixeles cuyo valor en sea entre 254 y 255
ret,th1 = cv2.threshold(gray,254,255,cv2.THRESH_BINARY)
#hago un kernel de 11x11 de unos. Los Kernels se acostumbra hacerse de tamaño no par y cuadrados
#para que se den una idea algo asi:
"""
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1
"""
kernel = np.ones((11,11), np.uint8) 
#aplico un filtro de dilatacion. Este filtro hace que los puntos blancos se expandan 
#provocando que algunos puntitos negros desaparecan 
#le pueden hacer un cv.imshow para que vean el resultado
th1 = cv2.dilate(th1,kernel,1)
kernel = np.ones((11,11), np.uint8) 
#Despues aplico uno de erosion que hace lo opuesto al de dilatacion
th1 = cv2.erode(th1,kernel,1)
#aplico un flitro gausiando de 5x5  para suavisar los bordes 
th1 = cv2.GaussianBlur(th1,(5,5),cv2.BORDER_DEFAULT)
#binarios la imagen
ret,th2 = cv2.threshold(th1,235,255,cv2.THRESH_BINARY)
th2 = cv2.dilate(th2,kernel,1)
th2 = cv2.cvtColor(th2,cv2.COLOR_GRAY2BGR)
#---- Trazo del grafo no dirigido ----
#Titulo deonde se imprimiran los vertices
print("Vertices:",end=" ")
#Itermaos sobre los vertices para su trazo en los mapas
for vertice in vertices:
    # Los parametros de la funcion circle son:
    # - imagne donde se van a pintar
    # - coordenada del centro del cisculo (x,y)
    # - radio del circulo
    # - color
    # - grosor de la linea (-1 es para pintar un circulo relleno)
    # Como los vertices vienen en fila columna para pintarlos en la imagen paso sus valores al reves 
    cv2.circle(th2,(vertice[1],vertice[0]),3,(255,0,0),-1)#Mapa binarizado
    cv2.circle(mapa,(vertice[1],vertice[0]),4,(255,0,0),-1)#Mapa del MST
    #Imprimimos los vertices en un mismo renglon
    print(vertice,end=" ")
print("\n")
#Conjunto de aristas dibujadas para evitar repetir aristas al trazarlas
aristas_dibujadas = set()
#Iteramos sobre todos los vertices
for i in range(num_vertices):
    #Iteramos sobre todos los vertices +1 para crear las aristas
    for j in range(i+1, num_vertices):
        # Antes de dibujar la línea, verificamos que no haya sido dibujada antes
        #Creamos tuplas de las aristas en nuestros indices por comodidad de operacion donde (v1,v2)==(v2,v1)
        arista_actual = (tuple(vertices[i]), tuple(vertices[j]))
        arista_inversa = (tuple(vertices[j]), tuple(vertices[i]))
        # Comprobar si las aristas ya han sido dibujadas
        if arista_actual not in aristas_dibujadas and arista_inversa not in aristas_dibujadas:
            # Si no esta en el set, la dibujamos
            dibujar_linea(vertices[i], vertices[j], th2)
            # Agregar las aristas al conjunto para mantener un registro
            aristas_dibujadas.add(arista_actual)
            aristas_dibujadas.add(arista_inversa)
#Mostramos la imagen con el grafo trazado
cv2.imshow('thres2',th2)
#------Implementacion del algoritmo de PRIM -MST------
#Se selecciona un vertice de partida de forma aleatoria y lo convertimos a formato de lista para poder operar con el
vertice_first = rd.choice(vertices)
arrayVerticeInicial=np.array(vertice_first)
vertice_inicial=arrayVerticeInicial.tolist()
#Imprimimos el vertice de partida
print("Punto de partida:",vertice_inicial)
#Lista de vertices no visitados
v_novisitados=[]
#Lista de vertices visitados
v_visitados=[]
#Agregamos el vertice inicial a la lista de vertices visitados
v_visitados.append(vertice_inicial)
#Lista de aristas del MST
mst=[]
#Lista de aristas junto a sus pesos
aristas_pesos=[]
#Ordenamos las aristas de forma ascendente junto a sus pesos, intentado no perder sus pares 
for i in range(len(aristas)):
    for j in range(i+1,len(aristas)):
        if pesos[j]<pesos[i]:#Nuestro criterio de ordenamiento es el peso de las aristas
            #Intercambiamos los pesos y las aristas
            pesos[i],pesos[j]=pesos[j],pesos[i]
            aristas[i],aristas[j]=aristas[j],aristas[i]

# Agregamos las aristas junto a sus pesos a una lista de tuplas en forma (arista,peso) y sin formato de numpy array
for i in range(len(aristas)):
    #Convertimos el arreglo de numpy a lista para operar con el
    arreglo=np.array(aristas[i])
    #Agregamos la arista junto a su peso a la lista
    aristas_pesos.append((arreglo.tolist(),pesos[i]))
'''
FORMATO DE LAS ARISTAS CON SUS PESOS
aristas_pesos=[((vertice1,vertice2),peso),((vertice1,vertice2),peso),((vertice1,vertice2),peso),...]
'''
#Mostramos las aristas junto a sus pesos
print("Aristas y sus pesos:",aristas_pesos)
#Iteramos sobre todos los vertices para obtener el MST
while(len(v_visitados)<num_vertices):#Mientras no hayamos visitado todos los vertices
    #Iteramos sobre las aristas junto a sus pesos
    for arista in aristas_pesos:
        #Desempaquetamos la arista
        v1,v2=arista[0]#Es arista[0] porque solo nos interesa la arista, no el peso, puesto que esta ordenada ascendentemente respecto al peso
        #Si v1 ya lo visitamos pero a v2 no
        if v1 in v_visitados and v2 not in v_visitados:
            #Lo agregamos a la lista de vertices visitados
            v_visitados.append(v2)
            #Lo agregamos a la lista de aristas del MST
            mst.append(arista)
            #Dibujamos la linea en el mapa
            dibujar_linea_mst(v1,v2,mapa)
            #Terminamos el ciclo para para iterar sobre el siguiente vertice
            break
        #Si ya visitamos a v2 pero no a v1
        elif v2 in v_visitados and v1 not in v_visitados:
            v_visitados.append(v1)
            mst.append(arista)
            dibujar_linea_mst(v1,v2,mapa)
            break
# Mostramos el MST, sus aristas con pesos
print("\nMST:",mst)
#Mostramos el mapa
cv2.imshow('PRIM',mapa)
#--- Destruccion de las ventanas ---
cv2.waitKey(0)
cv2.destroyAllWindows()
