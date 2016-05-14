#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Se abre archivo json usando libreria json
with open("C:/Users/Peter Mtz/Documents/School Work/PAPBLO/Proyecto Bienevales/escuelas.json") as data_file:
    data = json.load(data_file)
# Se pasa a dataframe
escuelas_df = pd.DataFrame.from_dict(data, orient='index', dtype=None)

# ---------------------------------Lugares de escuelas-----------------------------------------------------
num_cds = {};
# Ciclo para asignar un 0 a cada localidad
for key, value in dict.items(data):
    num_cds[value["localidad"]] = 0

# Ciclo para contar cuantas localidades hay
for key, value in dict.items(data):
    num_cds[value["localidad"]] = num_cds[value["localidad"]] + 1
print(num_cds)

# Se acomodan por orden las ciudades
L = num_cds.items()
L.sort(lambda x, y: cmp(y[1], x[1]))
print(L)
print(len(L))

# Ciclo para obtener los numeros en forma de vector
frequency_loc = []
cities = []
c = 0
for line in L:
    if c < 15:
        frequency_loc.append(line[1])
        cities.append(line[0])
    if c == 15:
        frequency_loc.append(line[1])
        cities.append("Otros")
    if c > 15:
        frequency_loc[15] = frequency_loc[15] + line[1]
    c = c + 1

# Se grafican los vectores de frecuencia y las ciudades
y_axis = np.arange(1, len(cities) + 1, 1)
plt.barh(y_axis, frequency_loc, align='center')
plt.yticks(y_axis, cities)
plt.show()

# ----------------para nivel de escuela---------------------
nivel = {};

for key, value in dict.items(data):
    nivel[value["nivel"]] = 0

# Ciclo para contar cuantas localidades hay
for key, value in dict.items(data):
    nivel[value["nivel"]] = nivel[value["nivel"]] + 1
print(nivel)

# Se acomodan por orden los niveles de educacion
vector_nivel = nivel.items()
vector_nivel.sort(lambda x, y: cmp(y[1], x[1]))
print(vector_nivel)
print(len(vector_nivel))

# Ciclo para obtener los numeros en forma de vector
frequency_niv = []
escolar = []

for line in vector_nivel:
    frequency_niv.append(line[1])
    escolar.append(line[0])

# Se grafican los vectores de frecuencia y las ciudades
y_axis = np.arange(1, len(escolar) + 1, 1)
plt.barh(y_axis, frequency_niv, align='center')
plt.yticks(y_axis, escolar)
plt.show()

# ---------------------Para Region------------------------------------------
# Region cienega esta mal en el archivo json, tener cuidado con eso
region = {};
# Ciclo para asignar un 0 a cada region
for key, value in dict.items(data):
    region[value["region"]] = 0

# Ciclo para contar cuantas regiones hay
for key, value in dict.items(data):
    region[value["region"]] = region[value["region"]] + 1

print(region)

# Se acomodan por orden las regiones
vector_reg = region.items()
vector_reg.sort(lambda x, y: cmp(y[1], x[1]))
print(vector_reg)
print(len(vector_reg))

# Ciclo para obtener los numeros en forma de vector
frequency_reg = []
reg = []

for line in vector_reg:
    frequency_reg.append(line[1])
    reg.append(line[0])

print(reg)
print(vector_reg)

# Se grafican los vectores de frecuencia y las ciudades
y_axis = np.arange(1, len(cities) + 1, 1)
plt.barh(y_axis, frequency_loc, align='center')
plt.yticks(y_axis, cities)
plt.show()


