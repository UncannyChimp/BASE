#Esto es un comentario
if 3 > 5:
    print("Esto no se va a interpretar")

#if 5 > 3:
    #print("Esto si se cumple")

x = 5
y = "chanchito feliz"

#print (x, y)

email = "chanchito feliz.com"

#print(email)

mivar = 'chanchito'
MIVAR = "chanchito"
a, b, c = "lala", "lele", "lili"

#print(a, b, c)

valor1 = valor2 = valor3 = "chanchito feliz"

#print (valor1, valor2, valor3)

inicio = "Hola "
final = "Mundo"

#print (inicio + final)



palabra = "hola mundo" #string
oracion = 'hola mundo comilla doble' #string

entero = 20 #integer
conDecimales = 20.2 #float
complejo = 1j

#print (palabra, oracion, entero, conDecimales, complejo)



lista = ["Hola", "Mundo", "Chanchito feliz"]
lista2 = lista.copy()
lista.append("Chanchito triste")
#lista.clear()
#print(lista, lista2.count(3))
#print(len(lista), len(lista2))
largoLista = len(lista)
largoLista2 = len(lista2)

#print(largoLista, largoLista2)

#print(lista[2])

# lista.po() # este elimina el ultimo valor de la lista
 #lista.remove("Hola") #Este elimina un elemento por su valor

lista.reverse()
lista.sort()
tupla = ("hola", "mundo", "somos", "tupla")
listaDeTupla = list(tupla)
listaDeTupla.append('Chanchito')
#print (listaDeTupla)

rango = range(6)
#print(rango)

diccionario = {
    "nombre": "Chanchito feliz",
    "raza" : "Persa",
    "Edad": 5 
}

#print(diccionario)
#print(diccionario["nombre"])
#print(diccionario["raza"])
#print(diccionario.get("nombre"))
diccionario["nombre"] = "Fluffy"

#print(len(diccionario))

diccionario["ronronea"] = "Si"

print(diccionario)
#diccionario.pop("ronronea")
#diccionario.popitem()
#copiaGatito = diccionario.copy()
copiaGatito = dict(diccionario)
#del diccionario["ronronea"]
diccionario.clear()
#print(diccionario, copiaGatito)

fluffy = {
    "nonbre": "Fluffy",
    "edad": 4
}

mamba = {
    "nombre": "Black mamba",
   "edad":12
}

gatitos = {
    "Fluffy" : fluffy,
    "Mamba" : mamba
}

print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad=6)
print(perritos)

verdadero = True
falso = False

print(verdadero, falso)