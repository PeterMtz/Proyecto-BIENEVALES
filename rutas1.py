import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import unicodedata
from collections import Counter

with open('C:/Users/Peter Mtz/Documents/School Work/PAPBLO/Proyecto Bienevales/rutas.json') as data_file:
    rutas = json.load(data_file)

rutas_df = pd.DataFrame.from_dict(rutas, orient='index', dtype=None)
rutas_df.describe()

with pd.option_context('display.max_rows', 10, 'display.max_columns', 50):
    print rutas_df

name = "empresa"
num = {}
for key, value in dict.items(rutas):
    num[value[name]] = 0
for key, value in dict.items(rutas):
    num[value[name]] = num[value[name]] + 1
print(num)
print(len(num))

# Se acomodan por orden
vector_escuela = num.items()
vector_escuela.sort(lambda x, y: cmp(y[1], x[1]))

# Ciclo para obtener los numeros en forma de vector
frequency_escuela = []
escuela = []
c = 0
for line in vector_escuela:
    if c < 10:
        frequency_escuela.append(line[1])
        escuela.append(line[0])
    if c == 10:
        frequency_escuela.append(line[1])
        escuela.append("Otros")
    if c > 10:
        frequency_escuela[10] = frequency_escuela[10] + line[1]
    c += 1

# Se grafican los vectores de frecuencia
y_axis = np.arange(1, len(cita) + 1, 1)
plt.barh(y_axis, frequency_escuela, align='center')
plt.yticks(y_axis, escuela)
plt.show()
