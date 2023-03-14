#Multiplicar dos números sin usar el simbolo de multiplicación

a = 4
b = 8
resultado = 0

for x in range(a):
    resultado += b

print (resultado)

#Ingresar nombre y apellido e imprimirlo al reves
nombre = 'Nicolas'
apellido = 'Feli'

concatenacion = nombre + ' ' +  apellido

print(concatenacion[::-1])

#Escribir una función que encuentre el elemento menor de una lista

lista = [1, 2, 5, 55, -24, -13]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('menor', menor)

#Escribir una funcion que devuelva el volumen de una esfera por su radio

def calcularVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calcularVolumen(6)
print(resultado)

#Escribir una función que indique si el usuario es mayor de edad

def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

print(resultado1, resultado2)

#Escribir una funcion que indique si un número es par o impar

def esPar(n):
    return n % 2 == 0

resultado = esPar(10)
print (resultado)

#Escribir una funcion que indique cuantas vocales tiene una palabra
palabra = 'ChanchitoFeliz'
vocales = 0
for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

print (vocales)

