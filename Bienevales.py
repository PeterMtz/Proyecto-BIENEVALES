import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import unicodedata
from collections import Counter



# Se abre archivo json usando libreria json
with open("C:/Users/Peter Mtz/Documents/School Work/PAPBLO/Proyecto Bienevales/bienevales.json") as data_file:
    vales = json.load(data_file)


# -----------------Operaciones con dataframe---------------------------------------
# Se transforma el diccionario en un dataframe ordenado por renglones
vales_df = pd.DataFrame.from_dict(vales, orient='index', dtype=None)
vales_df.describe()

# Imprimir del tamano que tu quieras
with pd.option_context('display.max_rows', 10, 'display.max_columns', 50):
    print vales_df

# Aqui estan colapsadas las listas
# ------ Lista con todos los datos de las tablets-----------------
lista_tablet = [v["has_tablet"] for v in vales.values()]
# Contar cuantos true y falses hay
sum_tablet_v = lista_tablet.count(True)
sum_tablet_f = lista_tablet.count(False)

# --------- Lista con todos los datos de major income---------------
lista_income = [v["major_income"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_income)

# --------Lista del neighborhood----------
lista_neighbor = [v["neighborhood"] for v in vales.values()]
Counter(lista_neighbor)

# Histograma del neighborhood separando los mayores
num_neighbor = {}
# Ciclo para asignar un 0 a cada cosa
for key, value in dict.items(vales):
    num_neighbor[value["neighborhood"]] = 0

# Ciclo para contar cuantas localidades hay
for key, value in dict.items(vales):
    num_neighbor[value["neighborhood"]] += 1

# Se acomodan por orden
vector_neighbor = num_neighbor.items()
vector_neighbor.sort(lambda x, y: cmp(y[1], x[1]))

# Ciclo para obtener los numeros en forma de vector
frequency_neighbor = []
neighbor = []
c = 0
for line in vector_neighbor:
    if c < 10:
        frequency_neighbor.append(line[1])
        neighbor.append(line[0])
    if c == 10:
        frequency_neighbor.append(line[1])
        neighbor.append("Otros")
    if c > 10:
        frequency_neighbor[10] = frequency_neighbor[10] + line[1]
    c += 1

# Se grafican los vectores de frecuencia
y_axis = np.arange(1, len(neighbor) + 1, 1)
plt.barh(y_axis, frequency_neighbor, align='center')
plt.yticks(y_axis, neighbor)
plt.show()

# -------------Lista del citizenship-------------
lista_citizen = [v["citizenship"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_citizen)

# -----------Lista del macromodulo--------------------
lista_modulo = [v["cita_macromodulo"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_modulo)

# --------------Lista del dialecto-----------------------
lista_dialec = [v["dialect"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_dialec)

# ---------------Lista de gastos transvales--------------
lista_transv = [v["expenses_transv"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_transv)

# ---------------Lista de municipios-----------------------
lista_municip = [v["municipality"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_municip)

# ----------------Lista de grado escolar-------------------
lista_school = [v["schooling"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_school)

# ------------------Lista de laptops-----------------------
lista_lap = [v["has_laptop"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_lap)

# ---------------------Lista de entrega dia---------------
lista_entreg = [v["entrega_dia_date"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_entreg)

# ----------------------Transporte rutas de camion------------
lista_rutas = [v["transporte_rutas"] for v in vales.values()]


# ---------------------Lista de citas---------------
lista_citas = [v["cita_dia"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_citas)

# -----------Lista de sig in ----------------------------
lista_sign = [v["sign_in_count"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_sign)

# ------------Lista de quien paga la escuela-------------
lista_edexp = [v["education_expenses"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_edexp)

# ---------------Lista de discapacitados------------------
lista_disc = [v["disability"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_disc)

# -----------------Lista de framacias---------------------
lista_farm = [v["pharmacy"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_farm)

# -----------------Lista de si es indigena---------------
lista_indi = [v["indian"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_indi)

# ------------------Lista de citizen---------------------
lista_citi = [v["citizen"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_citi)

# -----------------------Lista de fam income------------
lista_faminc = [v["family_income"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_faminc)

# ----------------------Lista de cita date-------------
lista_citdd = [v["cita_dia_date"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_citdd)

# ----------------------Lista hora macromodulo----------
lista_horam = [v["cita_hora_macromodulo"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_horam)

# -------------------------Lista del codigo postal------
lista_zip = [v["zip_code"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_zip)

# Histograma y agrupacion de los zip
num_zip = {}
# Ciclo para asignar un 0 a cada cosa
for key, value in dict.items(vales):
    num_zip[value["zip_code"]] = 0

# Ciclo para contar cuantas localidades hay
for key, value in dict.items(vales):
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
    if c == 10:
        frequency_zip.append(line[1])
        zipc.append("Otros")
    if c > 10:
        frequency_zip[10] = frequency_zip[10] + line[1]
    c += 1

# Se grafican los vectores de frecuencia
y_axis = np.arange(1, len(zipc) + 1, 1)
plt.barh(y_axis, frequency_zip, align='center')
plt.yticks(y_axis, zipc)
plt.show()

# -----------------Anio de nacimiento-------------------
lista_cumple = [v["birthday_year"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_cumple)

# Histograma de la edad
num_cumple = {}
# Ciclo para asignar un 0 a cada cosa
for key, value in dict.items(vales):
    num_cumple[value["birthday_year"]] = 0

# Ciclo para contar cuantas localidades hay
for key, value in dict.items(vales):
    num_cumple[value["birthday_year"]] += 1

# Se acomodan por orden
vector_cumple = num_cumple.items()
vector_cumple.sort(lambda x, y: cmp(y[1], x[1]))

# Ciclo para obtener los numeros en forma de vector
frequency_cumple = []
cumple = []
c = 0
for line in vector_cumple:
    if c < 10:
        frequency_cumple.append(line[1])
        cumple.append(line[0])
    if c == 10:
        frequency_cumple.append(line[1])
        cumple.append("Otros")
    if c > 10:
        frequency_cumple[10] = frequency_cumple[10] + line[1]
    c += 1

# Se grafican los vectores de frecuencia
y_axis = np.arange(1, len(cumple) + 1, 1)
plt.barh(y_axis, frequency_cumple, align='center')
plt.yticks(y_axis, cumple)
plt.show()

# --------------------Lista de hora macromodulo------------------
lista_horam = [v["cita_hora_macromodulo"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_horam)

# ------------------Lista de indigenas------------------------------
lista_indigen = [v["indigenous_community"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_indigen)

# -----------------Lista de grado-----------------------------------
lista_degree = [v["degree"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_degree)

# ------------Lista entrega macromodulo----------------------------
lista_entmac = [v["entrega_hora_macromodulo"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_entmac)

# -------------Lista cita modulo----------------------------------
lista_cmod = [v["cita_modulo"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_cmod)

# Histograma de la edad
num_cita = {}
# Ciclo para asignar un 0 a cada cosa
for key, value in dict.items(vales):
    num_cita[value["cita_modulo"]] = 0

# Ciclo para contar cuantas localidades hay
for key, value in dict.items(vales):
    num_cita[value["cita_modulo"]] = num_cita[value["cita_modulo"]] + 1

# Se acomodan por orden
vector_cita = num_cita.items()
vector_cita.sort(lambda x, y: cmp(y[1], x[1]))

# Ciclo para obtener los numeros en forma de vector
frequency_cita = []
cita = []
c = 0
for line in vector_cita:
    if c < 10:
        frequency_cita.append(line[1])
        cita.append(line[0])
    if c == 10:
        frequency_cita.append(line[1])
        cita.append("Otros")
    if c > 10:
        frequency_cita[10] = frequency_cita[10] + line[1]
    c += 1

# Se grafican los vectores de frecuencia
y_axis = np.arange(1, len(cita) + 1, 1)
plt.barh(y_axis, frequency_cita, align='center')
plt.yticks(y_axis, cita)
plt.show()

# -------------Lista de seguro------------------------------
lista_entdi = [v["entrega_dia"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_entdi)

# ----------------Lista si tiene compu-------------------------
lista_compu = [v["has_pc"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_compu)

# -------------------Lista celular----------------------------
lista_cel = [v["has_celphone"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_cel)

# ------------Lista de nombre dialecto-----------------------
lista_ndial = [v["dialect_name"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_ndial)

# ------------Lista escuela donde va-------------------------
lista_escuela = [v["school"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_escuela)
# Histograma de la escuela
num_escuela = {}
# Ciclo para asignar un 0 a cada cosa
for key, value in dict.items(vales):
    num_escuela[value["school"]] = 0

# Ciclo para contar cuantas localidades hay
for key, value in dict.items(vales):
    num_escuela[value["school"]] += 1

# Se acomodan por orden
vector_escuela = num_escuela.items()
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

# -----------------Genero----------------------------
lista_gen = [v["gender"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_gen)

# -----------------Estado civil----------------------------
lista_edocv = [v["marital_status"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_edocv)

# -----------------Tipo discapacidad----------------------------
lista_tdis = [v["type_disability"] for v in vales.values()]
# Contar que cosas hay en la lista y cuantas se repiten
Counter(lista_tdis)

# Aqui estan colapsadas los arreglos
# ------------------Limpieza de datos----------------------------------------------
# Arreglar los datos de income
for index, item in enumerate(lista_income):
    if not ((item == "PADRE") or (item == "MADRE") or
            (item == "HIJA/HIJO") or (item == "AMBOS")):

        lista_income[index] = "OTROS"

# Arreglar los datos de neighborhood
for index, item in enumerate(lista_neighbor):

    if (item == " ") or (item == "") or (item == "#N/A") or (item == None):
        lista_neighbor[index] = "SIN INFORMACION"

    if type(lista_neighbor[index]) == unicode:
        lista_neighbor[index] = unicodedata.normalize('NFKD',
                                                      lista_neighbor[index]).encode('ascii', 'ignore')


# Arreglar los datos de municipio
for index, item in enumerate(lista_municip):

    if (item == " ") or (item == "") or (item == "#N/A") or (item == None):
        lista_municip[index] = "SIN INFORMACION"

    # Si son unicode los pasa a strings
    if type(lista_municip[index]) == unicode:

        lista_municip[index] = unicodedata.normalize('NFKD',
                                                     lista_municip[index]).encode('ascii', 'ignore')
        # Lo que empiece con esto, le pondra aquello
        if lista_municip[index].startswith("TLAJO"):
            lista_municip[index] = "TLAJOMULCO DE ZUNIGA"

        if lista_municip[index].startswith("IXTLAHUA"):
            lista_municip[index] = "IXTLAHUACAN DE LOS MEMBRILLOS"

        if lista_municip[index].startswith("TONAL"):
            lista_municip[index] = "TONALA"

        if lista_municip[index].startswith("JUANA"):
            lista_municip[index] = "JUANACATLAN"

# Arreglar datos de schooling
for index, item in enumerate(lista_school):

    if (item == " ") or (item == "") or (item == "#N/A") or (item == None):
        lista_school[index] = "SIN INFORMACION"

    if type(lista_school[index]) == unicode:
        lista_school[index] = unicodedata.normalize('NFKD',
                                                    lista_school[index]).encode('ascii', 'ignore')


# Arreglar datos de education expenses
for index, item in enumerate(lista_edexp):

    if (item == " ") or (item == "") or (item == "#N/A")\
            or (item == None) or (item == "NO TIENE") or (item == "0"):
        lista_edexp[index] = "SIN INFORMACION"

    if type(lista_edexp[index]) == unicode:
        lista_edexp[index] = unicodedata.normalize('NFKD',
                                                   lista_edexp[index]).encode('ascii', 'ignore')
        # Lo que empiece con esto, le pondra aquello
        if lista_edexp[index].startswith("P"):
            lista_edexp[index] = "PADRE"

        if lista_edexp[index].startswith("A"):
            lista_edexp[index] = "AMBOS"

# Arreglar datos de disability
for index, item in enumerate(lista_disc):
    if not (item == True):
        lista_disc[index] = False

# Arreglar datos de birthday
for index, item in enumerate(lista_cumple):

    if (item == " ") or (item == "") or (item == "#N/A")\
            or (item == None) or (item == 0):
        lista_cumple[index] = np.nan

# Arreglar datos de cita modulo
for index, item in enumerate(lista_cmod):

    if (item == "0") or (item == "#N/A") or (item == None):
        lista_cmod[index] = "SIN INFORMACION"

    # Si son unicode los pasa a strings
    if type(lista_cmod[index]) == unicode:
        lista_cmod[index] = unicodedata.normalize('NFKD',
                                                  lista_cmod[index]).encode('ascii', 'ignore')
        # Lo que empiece con esto, le pondra aquello
        if lista_cmod[index].startswith("CENTRO"):
            lista_cmod[index] = "CENTRO"

        if lista_cmod[index].startswith("LAS"):
            lista_cmod[index] = "LAS AGUILAS(UNIDAD ADMINISTRATIVA DE ZAPOPAN)"

        if lista_cmod[index].startswith("POLI"):
            lista_cmod[index] = "POLITECNICO(UDG)"

        if lista_cmod[index].startswith("SAN"):
            lista_cmod[index] = "SAN ANDRES(UNIDAD ADMINISTRATIVA DE ZAPOPAN)"

        if lista_cmod[index].startswith("VIAL"):
            lista_cmod[index] = "VIALIDAD(SECRETARIA DE MOVILIDAD)"


# Arreglar datos de genero
for index, item in enumerate(lista_gen):
    if (item == "#N/A") or (item == None):
        lista_gen[index] = "SIN INFORMACION"

# arreglamos la lista de edo civil
for index, item in enumerate(lista_edocv):

    if (item == "#N/A") or (item == None):
        lista_edocv[index] = "SIN INFORMACION"

    # Si son unicode los pasa a strings
    if type(lista_edocv[index]) == unicode:

        lista_edocv[index] = unicodedata.normalize('NFKD',
                                                   lista_edocv[index]).encode('ascii', 'ignore')
        # Lo que empiece con esto, le pondra aquello
        if lista_edocv[index].startswith("UNI"):
            lista_edocv[index] = "UNION LIBRE"

# Agregar cuantos camiones toma al dia
rutas = [v["transporte_rutas"] for v in vales.values()]

for index, item in enumerate(rutas):

    if (item == " ") or (item == "") or (item == "#N/A") or (item == None):
        rutas[index] = "0"

#print(len(rutas))

lista_camiones = []
for elemento in (rutas):
    lista_camiones.append(len(elemento))

# -------------Unir los datos en un solo dataframe-----------------------------------
# Obtenemos los indices
indices = list(vales_df.index)
# Unimos las listas
vales_limpio = pd.DataFrame({'id': indices, 'tablet': lista_tablet,
                             'income': lista_income,
                             'neighborhood': lista_neighbor,
                             "municipality": lista_municip,
                             "schooling_level": lista_school,
                             "laptop": lista_lap,
                             "sign_in_count": lista_sign,
                             "education_expenses": lista_edexp,
                             "disability": lista_disc,
                             "zip_code": lista_zip,
                             "birthday": lista_cumple,
                             "citamodulo": lista_cmod,
                             "computer": lista_compu,
                             "gender": lista_gen,
                             "edocivil": lista_edocv,
                             "num_camiones": lista_camiones})

# Se acmodan las columnas para que esten en el orden original
vales_limpio = vales_limpio.reindex(columns=["id", "tablet", "income", "neighborhood",
                                             "municipality", "schooling_level", "laptop",
                                             "sign_in_count", "education_expenses", "disability",
                                             "zip_code", "birthday", "citamodulo", "computer",
                                             "gender", "edocivil", "num_camiones"])

vales_limpio.to_csv("C:/Users/Peter Mtz/Documents/School Work/PAPBLO/Proyecto Bienevales/vales_limpio.csv")

plt.hist(vales_limpio.birthday)
plt.show()


