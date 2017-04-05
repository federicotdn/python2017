# Los comentarios se escriben poniendo '#' al comienzo de la linea
# Los comentarios son ignorados por el interprete

print(type(100))
print(type("Hello, World!"))
print(type(True))
print(type(""))
print(type(0))
print(type(739.233))
print(type(-1))
print(type(False))
print(type("100"))
print(type("True"))
print(type(15.0))
print(type(None))

print("-------------------") # imprimir un separador para leer los resultados mas facilmente

# Pruebas con asignacion y expresiones

a = 1
b = a
a = 2
print(a)
print(b)
print(type(a))
print(type(b))

print("-------------------")

a = 10 // 3
print(type(a))
b = a + 1
print(b)

print("-------------------")

c = "1"
d = "2"
e = c + d
print(e)
print(type(e))

print("-------------------")

a = 10
a = a + 1
print(a)

print("-------------------")

width = 2
print(width / 2)
print(width / 2.0)
print(width // 2)

print("-------------------")

# PEMDAS
print((1 + 2 / 4) + 3 * 2 ** 3)