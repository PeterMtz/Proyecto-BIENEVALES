import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

diccionario=Counter(lista_gen)
diccionario_income=Counter(lista_income)
diccionario_munic=Counter(lista_municip)
diccionario_school=Counter(lista_school)
diccionario_disc=Counter(lista_disc)
diccionario_modu=Counter(lista_cmod)
diccionario_edo=Counter(lista_edocv)


L = diccionario.items()
L.sort(lambda x,y:cmp(y[1], x[1]))
print(L)
print(len(L))


freequency = []
cities = []
c = 0
for line in L:
	if c < 11:
		freequency.append(line[1])
		cities.append(line[0])
	if c == 11:
		freequency.append(line[1])
		cities.append("Otros")
	if c > 11:
		freequency[11] = freequency[11] + line[1]
	c = c + 1

colors = ['#624ea7', 'r', 'yellow']

y_axis = np.arange(1, len(cities) + 1, 1)
plt.barh(y_axis, freequency, align='center', color=colors)
plt.yticks(y_axis, cities)
plt.ylabel("Genero")
plt.title("Hombres y mujeres que usan bienevales")
plt.xlabel("Cantidad de personas")
plt.show()

#-------------------

num_zip = {}
# Ciclo para asignar un 0 a cada cosa
for key, value in dict.items(data):
    num_zip[value["zip_code"]] = 0

# Ciclo para contar cuantas localidades hay
for key, value in dict.items(data):
    num_zip[value["zip_code"]] += 1


# Se acomodan por orden
vector_zip = num_zip.items()
vector_zip.sort(lambda x, y: cmp(y[1], x[1]))


# Ciclo para obtener los numeros en forma de vector
frequency_zip = []
zipc = []
c = 0
for line in vector_zip:
    if c < 10:
        frequency_zip.append(line[1])
        zipc.append(line[0])
    c += 1

# Se grafican los vectores de frecuencia
colors=['olivedrab','chartreuse','darksage','lightgreen','forestgreen','olive','lime','sage','g','darkkhaki']
y_axis = np.arange(1, len(zipc) + 1, 1)
plt.barh(y_axis, frequency_zip, align='center', color=colors)
plt.yticks(y_axis, zipc)
plt.ylabel("Zipcodes")
plt.title("Top 10 Zipcodes")
plt.xlabel("Cantidad de personas")
plt.show()

#--------------

num_zip = {}
# Ciclo para asignar un 0 a cada cosa
for key, value in dict.items(data):
    num_zip[value["birthday_year"]] = 0

# Ciclo para contar cuantas localidades hay
for key, value in dict.items(data):
    num_zip[value["birthday_year"]] += 1


# Se acomodan por orden
vector_zip = num_zip.items()
vector_zip.sort(lambda x, y: cmp(y[1], x[1]))


# Ciclo para obtener los numeros en forma de vector
frequency_zip = []
zipc = []
c = 0
for line in vector_zip:
    if c < 10:
        frequency_zip.append(line[1])
        zipc.append(line[0])
    c += 1

# Se grafican los vectores de frecuencia
colors=['mediumorchid','purple','fuchsia','hotpink','pink','darkmagenta','orchid','lightpink','plum','m']
y_axis = np.arange(1, len(zipc) + 1, 1)
plt.barh(y_axis, frequency_zip, align='center', color=colors)
plt.yticks(y_axis, zipc)
plt.ylabel("birthday")
plt.title("Top10 bithday years")
plt.xlabel("Cantidad de personas")
plt.show()

#-----


L = diccionario_munic.items()
L.sort(lambda x,y:cmp(y[1], x[1]))
print(L)
print(len(L))


freequency = []
cities = []
c = 0
for line in L:
	if c < 10:
		freequency.append(line[1])
		cities.append(line[0])

colors = ['blue', 'midnightblue', 'b','navy','royalblue']

y_axis = np.arange(1, len(cities) + 1, 1)
plt.barh(y_axis, freequency, align='center', color=colors)
plt.yticks(y_axis, cities)
plt.ylabel("Municipio")
plt.title("Top10 Municipios")
plt.xlabel("Cantidad de personas")
plt.show()

#-----


L = diccionario_school.items()
L.sort(lambda x,y:cmp(y[1], x[1]))
print(L)
print(len(L))


freequency = []
cities = []
c = 0
for line in L:
	if c < 10:
		freequency.append(line[1])
		cities.append(line[0])

colors = ['peru', 'chocolate', 'burlywood','goldenrod','tan']

y_axis = np.arange(1, len(cities) + 1, 1)
plt.barh(y_axis, freequency, align='center', color=colors)
plt.yticks(y_axis, cities)
plt.ylabel("Escolaridad")
plt.title("Escolaridad")
plt.xlabel("Cantidad de personas")
plt.show()


#-----


L = diccionario_disc.items()
L.sort(lambda x,y:cmp(y[1], x[1]))
print(L)
print(len(L))


freequency = []
cities = []
x=["No tiene","Si tiene"]
c = 0
for line in L:
	if c < 10:
		freequency.append(line[1])
		cities.append(line[0])

colors = ['firebrick','darkblue']

y_axis = np.arange(1, len(cities) + 1, 1)
plt.barh(y_axis, freequency, align='center', color=colors)
plt.yticks(y_axis, x)
plt.ylabel("Si Tiene o no tiene")
plt.title("Personas con discapacidad")
plt.xlabel("Cantidad de personas")
plt.show()
#--------------

#-----

L = diccionario_modu.items()
L.sort(lambda x,y:cmp(y[1], x[1]))
print(L)
print(len(L))


freequency = []
cities = []
c = 0
for line in L:
	if c < 10:
		freequency.append(line[1])
		cities.append(line[0])


colors = ['mediumaquamarine','mediumturquoise','darkslategray','c','cadetblue','skyblue','dodgerblue','lightskyblue','steelblue','aqua']

y_axis = np.arange(1, len(cities) + 1, 1)
plt.barh(y_axis, freequency, align='center', color=colors)
plt.yticks(y_axis, cities)
plt.ylabel("Modulos")
plt.title("Top10 Modulos")
plt.xlabel("Cantidad de personas")
plt.show()
#--------------



L = diccionario_edo.items()
L.sort(lambda x,y:cmp(y[1], x[1]))
print(L)
print(len(L))


freequency = []
cities = []
c = 0
for line in L:
	if c < 10:
		freequency.append(line[1])
		cities.append(line[0])


colors = ['moccasin','tan','bisque','sienna','floralwhite']

y_axis = np.arange(1, len(cities) + 1, 1)
plt.barh(y_axis, freequency, align='center', color=colors)
plt.yticks(y_axis, cities)
plt.ylabel("Edo Civil")
plt.title("Estado Civil")
plt.xlabel("Cantidad de personas")
plt.show()
#--------------

zip45180 = 0
for index, row in vales.iterrows():
    if row["Edo"] == "FALSE" and row["zip"] == 45180 :
        zip45180= zip45180 + 1
#-----------------------