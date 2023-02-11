#Ejercicio, realizar un pedido de datos y de informacion

class Usuario:
    def __init__(self, nombre, apellido, clave, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.clave = clave
        self.edad = edad


def funcionPregunta(accion):
    print ("\na)\t Obtener informacion \nb)\t Leer datos")
    accion = input("\nQue desea realizar: ")
    return accion

def funcionMuestra(accion):
    if accion == "a":
        print ("Elegiste obtener informacion")
    elif accion == "b":
        print ("Elegiste leer datos")
    else:
        print("No reconozco la eleccion")

def main():
    accion = ""
    accion = funcionPregunta(accion)
    funcionMuestra(accion)
    print (accion)

main()