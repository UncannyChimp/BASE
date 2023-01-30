#dato = input("Ingrese dato: ")

#lista = ["hola", "mundo", "chanchito", "feliz", "dragones"]

#if lista.count(dato) > 0:
#    print("El dato existe", dato)
#else:
    #print("El dato no existe :(",dato)

primero = input("Ingrese primer número: " )

try:
    primero = int(primero)
except:
    primero = "chanchito feliz"

if primero=="chanchito feliz":
    print("El valor ingresado no es un entero")
    exit()

segundo = input("Ingrese segundo número: ")

try:
    segundo = int(segundo)
except:
    segundo = "chanchito feliz"

if primero=="chanchito feliz":
    print("El valor ingresado no es un entero")
    exit()

print("Que operación desea hacer: \n 1)Suma(+)\t2)Resta(-)\t3)Multiplicar(*)\t4)Dividir(/)  ")

operacion = input("\nOperación: ")

if operacion == "+" or operacion == "1":
    print(primero + segundo)
elif operacion == "-" or operacion == "2":
    print(primero - segundo)
elif operacion == "*" or operacion == "3":
    print(primero * segundo)
elif operacion == "/" or operacion == "4":
    print (primero / segundo)
else :
    print ("Operacion incorrecta")