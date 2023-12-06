"""
    Tarea 11. Comparación de algoritmos
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import random
import matplotlib.animation as manimation
import os

print(os.getcwd(),"-------")
random.seed(10)
np.random.seed(10)

def bubbleSort(arr2):
    it=0
    for i in range(len(arr2)):
        for j in range(len(arr2)-1):
            it+=1
            if arr2[j]>arr2[j+1]:
                arr2[j],arr2[j+1]=arr2[j+1],arr2[j]
    return arr2,it

def merge(arr1,arr2,it):
    arr=[]#aux array
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        it+=1
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while i<len(arr1):
        arr.append(arr1[i])
        i+=1
    while j<len(arr2):
        arr.append(arr2[j])
        j+=1
    return arr,it
def mergeSort(arr, it):
    if len(arr)<2:#Casos base
        return arr,it
    else:
        mitad=len(arr)//2
        arr1,it=mergeSort(arr[:mitad],it)
        arr2,it=mergeSort(arr[mitad:],it)
        return merge(arr1,arr2,it)

elementNumArray=[100,200,400,800,1600,3200,6400,12800]
tiemposMe=[]
iteracionesMe=[]
tiemposBu=[]
iteracionesBu=[]
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Bubble Sort vs Merge Sort', artist='Roodrigo Villaseñor',comment='Deja tu  like')
writer = FFMpegWriter(fps=24, metadata=metadata)
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(16,8))
ax1.title.set_text('Bubble Sort')
ax2.title.set_text('Merge Sort')
ax1.set_ylabel("No. de interaciones")
ax1.set_xlabel("# Elementos")
ax2.set_xlabel("# Elementos")             
with writer.saving(fig, "BubbleSortVsMergeSort.mp4", 100):
    plt.ion()
    for idx,elementNum in enumerate(elementNumArray):
        lista=np.random.randint(0,elementNum,elementNum)
        
        arr = lista.copy()
        start=time.time()
        itMerge=0
        elemento,it=mergeSort(arr,itMerge)
        finish=time.time()
        iteracionesMe.append(it)
        tiemposMe.append(finish-start)
        print("Merge Sort: ",it," iteraciones")
        print("Arreglo ordenado: ",elemento)

        arr2 = lista.copy()
        start=time.time()
        elemento,it=bubbleSort(arr2)
        finish=time.time()
        iteracionesBu.append(it)
        tiemposBu.append(finish-start)
        print("Bubble Sort: ",it," iteraciones")
        print("Arreglo ordenado: ",elemento)
        
        ax1.plot(elementNumArray[:idx+1], iteracionesBu, 'b-',label='Bubble Sort')
        ax2.plot(elementNumArray[:idx+1], iteracionesMe, 'g--',label='Merge Sort')
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.show(block=False)
        time.sleep(1)
        for i in range(24):
        writer.grab_frame()
