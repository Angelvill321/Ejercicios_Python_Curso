# Practico 10

from random import randint
from functools import reduce
lst = ['Aruba', 'Jamaica', 'Bermuda', 'Bahama', 'Key Largo', 'Montigo']

# Lista Comprension que tenga el primer caracter de cada palabra
milistacar = [pais[0] for pais in lst]
print('Primeros caracteres: ', milistacar)

# Lista Compresion que contenga la longitud de cada palabra
milistalong = [len(pais) for pais in lst]
print('Longitud de cada palabra: ', milistalong)

# Utilizar Reduce para calcular el total de caracteres que contienen todas las palabras de la lista lst
milistasuma = reduce(
    lambda x, y: x + len(y),
    lst, 0
)

print('Total de caracteres de la lista: ', milistasuma)

# Utilizando las rutinas random crear lista por compresion que contenga 50 numeros al azar, enteros, entre 1 y 100
random = [randint(1, 100) for _ in range(50)]
print('Los valores aleatorios son:', random)


# Filter crear una lista que contenga solo los mayores a 50 y otra solo los menores o igual a 50
menor50 = list(
    filter(
        lambda x:
        x > 50,
        random
    )
)
print('Lista mayores a 50: ', menor50)

mayoroigual50 = list(
    filter(
        lambda x:
        x <= 50,
        random
    )
)

print('Lista menores o igual a 50: ', mayoroigual50)

# Map para crear lista que contenga todos los numeros impares pero con el signo invertido (negativos)
impares = list(
    map(
        lambda x: -x if x % 2 != 0 else x,
        random
    )
)

print('Lista de Impares Negativos: ', impares)

# Reduce para la sumatoria de la lista generada en el item anterior
randomsuma = reduce(
    lambda x, y: x + y,
    random
)

print('Lista de suma de numeros random: ', randomsuma)

# Crear archivo de txt 'archivo.txt' en mosdo escritura

open('datos.txt', 'w')

# Escribir 3 lineas seaparas con las siguientes frases:
# Estamos quedandonos sin espacio y los unicos espacios a los que podemos ir son otros mundos.
# Solo somos una raza avanzada de monos del planeta menor de una estrella promedio.
# Si entendies el Universo, de alguna forma lo controlas.
# Cerrar archivo


def grabar_lineas():
    m = open('datos.txt', 'wt')
    m.write('Estamos quedandonos sin espacio y los unicos espacios a los que podemos ir son otros mundos.\n')
    m.write('Solo somos una raza avanzada de monos del planeta menor de una estrella promedio.\n')
    m.write('Si entendies el Universo, de alguna forma lo controlas.\n')
    m.close()


grabar_lineas()

# Abrir el archivo de texto creado en modo lectura


def leer_todo():
    m = open('datos.txt', 'r')
    todo = m.read()
    print(todo)
    m.close()


leer_todo()

# Leer de una por vez, cada linea del archivo en modo lectura


def leer_lineas():
    m = open('datos.txt', 'r')
    linea1 = m.readline()
    linea2 = m.readline()
    linea3 = m.readline()
    print(linea1, end='')
    print(linea2, end='')
    print(linea3)


leer_lineas()

# Grabar en una variable la longitud de cada linea de texto


def grabar_long():
    m = open("datos.txt", 'r')
    for line in m:
        print(len(line), end='\n')


grabar_long()
