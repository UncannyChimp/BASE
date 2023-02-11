def miFuncion():
    print("Mi primera funcion")

#miFuncion()

#def imprimeDato(nombre, apellido):
#    print("El nombre completo es", nombre, apellido)

#imprimeDato("Chanchito", "Feliz")

def mandaLista(*variable):
    print("La lista de variables mandadas es", variable[1])

#mandaLista("Mira","Todo","Esto", "Lo", "Imprime")

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

#nombreCompleto(nombre="Chanchito", apellido="Feliz")

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

#nombreCompleto2(nombre="Chanchito", apellido="Feliz")

def miFuncion2(argumento = 'Chanchito'):
    print(argumento)

#miFuncion2('BATMAN')
#miFuncion2()

def miFuncionLista(lista):
    for el in lista:
        print(el)

#miFuncionLista(['chanchito', 'feliz'])

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
        return i

#nombres = concatenaNombres(['chanchito', 'feliz'])
#print(nombres)

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i -1)

recursion(6)