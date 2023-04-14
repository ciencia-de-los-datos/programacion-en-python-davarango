"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import itertools
from collections import Counter
from datetime import datetime
from operator import itemgetter

with open ("data.csv", "r") as file:
        datos = file.readlines()
datos = [line.replace('\t','|').replace('\n','') for line in datos]
datos = [line.split('|') for line in datos]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    
    suma = 0
    for lista in datos:
        suma += int(lista[1])
    
    return suma


def pregunta_02():

    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
        
    columna = [fila[0] for fila in datos]
    columna_no_duplicadas = sorted(set(columna))
    lista_tupla =[(j, columna.count(j)) for j in columna_no_duplicadas]
    return lista_tupla
    

def pregunta_03():
    
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    datos_suma=[]
    
    for i, j in itertools.groupby(sorted(datos), lambda x : x[0]):
        datos_suma.append((i, sum(int(x[1]) for x in j)))

    return datos_suma


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    
    data_by_month = Counter()

    for row in datos:

        date = datetime.strptime(row[2][:7], "%Y-%m")
        data_by_month['{:02d}'.format(date.month)] += 1

    return sorted(list(data_by_month.items()))


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    datos_suma = []

    for i, j in itertools.groupby(sorted(datos), lambda x : x[0]):
        valores_list = [x[1] for x in j]
        datos_suma.append((i, int(max(valores_list)), int(min(valores_list))))

    return datos_suma



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    nueva_lista_valores = []
    datos_dic = []
    valores = [x[4] for x in datos]
    lista_valores = [x.split(",") for x in valores]

    for x in lista_valores:
        for y in x:
            nueva_lista_valores.append(y.split(":"))

    for i, j in itertools.groupby(sorted(nueva_lista_valores), lambda x : x[0]):
            valores_list = [int(x[1]) for x in j]
            datos_dic.append((i, min(valores_list), max(valores_list)))

    return datos_dic


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    columnas = [x[:2] for x in datos]
    new_group = []

    for i, j in itertools.groupby(sorted(columnas, key = lambda x: x[1]), lambda x: x[1]):
        new_group.append((int(i), [x[0] for x in j]))

    return new_group


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    columnas = [x[:2] for x in datos]
    new_group = []

    for i, j in itertools.groupby(sorted(columnas, key = lambda x: x[1]), lambda x: x[1]):
        new_group.append((int(i), sorted(list(set([x[0] for x in j])))))

    return new_group


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    nueva_lista_valores = []
    valores = [x[4] for x in datos]
    lista_valores = [x.split(",") for x in valores]
    contador = Counter()

    for x in lista_valores:
        for y in x:
            nueva_lista_valores.append(y.split(":"))

    for dicc in nueva_lista_valores:
        contador[dicc[0]] += 1

    return dict(sorted(contador.items()))



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    columnas = [itemgetter(0,3,4)(i) for i in datos]
    conteo = []
    for x in columnas:

        col4 = len(x[1].split(","))
        col5 = len(x[2].split(","))
        conteo.append((x[0],col4,col5))

    return conteo


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    
    col1 = [itemgetter(1)(i) for i in datos]
    col3 = [i[3].split(",") for i in datos]

    new_ = zip(col1,col3)
    new_1 = []
    new_group = []

    for x in list(new_):
        for y in x[1]:
            new_1.append((x[0],y))

    for i, j in itertools.groupby(sorted(new_1, key = lambda x: x[1]), lambda x: x[1]):
        new_group.append((i, sum([int(y[0]) for y in j])))

    return dict(new_group)



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    
    col0 = [itemgetter(0)(i) for i in datos]
    col4 = [i[4].split(",") for i in datos]

    valores = []
    a = 0
    for x in col4:
        for y in x:
            a += (int(y[y.index(":")+1:]))
        valores.append(a)
        a = 0

    new_ = zip(col0,valores)
    new_group = []

    for i, j in itertools.groupby(sorted(list(new_), key = lambda x: x[0]), lambda x: x[0]):
        new_group.append((i, sum(y[1] for y in j)))

    return dict(new_group)
