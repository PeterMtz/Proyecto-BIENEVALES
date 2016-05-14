import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import unicodedata
from matplotlib.pylab import hist, show

with open('C:/Users/Peter Mtz/Documents/School Work/PAPBLO/Proyecto Bienevales/bienevales.json') as data_file:
    vales = json.load(data_file)

rutas = [v["transporte_rutas"] for v in vales.values()]

for index, item in enumerate(rutas):

    if (item == " ") or (item == "") or (item == "#N/A") or (item == None):
        rutas[index] = "0"

print(len(rutas))

lista_camiones = []
for elemento in rutas:
    lista_camiones.append(len(elemento))

hist(lista_camiones, 10, (0, 10))
show()

L = [r for subl in rutas for r in subl]
df_rutas = pd.DataFrame.from_dict(c, orient='index', dtype=None)