import numpy as np

# Carga el archivo .npy
data = np.load('mapaProfundidad2.npy')

# Configura las opciones de impresión para mostrar el contenido completo
np.set_printoptions(threshold=np.inf)

# Imprime los datos
print(data)