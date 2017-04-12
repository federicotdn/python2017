# definicion de la funcion print_countdown

def print_countdown():
    print("3")
    print("2")
    print("1")
    print("Go!")

print_countdown() # invocar a la funcion

test = 1
test = print_countdown
test() # se invoca a print_countdown

print("----------------------------------")

# ------------- Parametros y Argumentos -------------

# definicion de print_twice

def print_twice(text):
    print(text)
    print(text)

print_twice("Hola") # invocar a print_twice
# print(text) -> esto NO funcionaria

# def increase_by_one(n):
#    ...

number = 10
# increase_by_one(number) -> no podria modificar a number

print("----------------------------------")

# ------------- Parametros Default -------------

def print_repeated(text, n = 2):
    print((text + ' ') * n)

print_repeated("Hola", 3)
print_repeated("Chau")

print("----------------------------------")

# ------------- Valor de Retorno -------------

def circle_area(r):
    return r ** 2 * 3.1416

radius = 2.2
area = circle_area(radius)

print(area)

test = print_twice("Hola") # test apunta a None

print("----------------------------------")

# ------------- Aridad e Invocacion -------------

def add_three(a, b, c):
    return a + b + c

print(add_three(1, 44, 100)) # imprime 145
# print(add_three(1)) -> TypeError
# print(add_three(1, 2, 3, 4)) -> TypeError

print("----------------------------------")

# ------------- Variables Locales -------------

def distance_squared(x1, y1, x2, y2):
    xdiff = (x2 - x1) ** 2
    ydiff = (y2 - y1) ** 2
    return xdiff + ydiff

test = distance_squared(1, 1, 2, 2)

print(test) # imprime 2
# print(xdiff) -> NO funcionaria

print("----------------------------------")

# ------------- Variables Globales -------------

test = 1

def modify_global():
    global test
    test = 100 # asignar 100 a test
    print(test)

modify_global()

print(test) # Imprime 100

print("----------------------------------")

# ------------- Funciones Puras -------------

def functionA(n):
    return n + 1

print(functionA(1))

print(functionA(1))

counter = 0

def functionB(n):
    global counter
    counter += 1
    return n + counter

print(functionB(1))

print(functionB(1))

print("----------------------------------")

# ------------- Sentencia Import -------------
from math import pi
print(pi)

import random as r
print(r.randint(0, 100))

from time import * # no se recomienda
print(time())
