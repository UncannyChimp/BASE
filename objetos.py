class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print("Hola!, mi nombre es ", self.nombre, self.apellido)


class Admin(Usuario):
    def superSaludo(self):
        print("Hola, me llamo", self.nombre, "y soy admin")

usuario = Usuario("Juan", "Quintero")

# usuario.saludo()
# usuario.nombre = "Chanchito"
# usuario.saludo()

# #-----------Eliminar cosas-------------------
# # del usuario.nombre 
# # usuario.saludo()
# # del usuario

# admin = Admin("Super", "Admin")
# admin.saludo()
# admin.superSaludo()

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya 
    def saludo(self):
        print ("Hola, soy un", self.tipo, "y mi sonido es el", self.onomatopeya)   

class Gato(Animal):
    tipo = "gato"
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print("Hola soy un gato extendido")

class Perro(Animal):
    tipo = "perro"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("Instanciando un perro")

class Canario(Animal):
    tipo = "canario"

gato = Gato("Fluppy", "Maullido")
gato.saludo()

perro = Perro("Firulais", "Ladrido")
perro.saludo()

canario = Canario("Piolin", "Silbido")
canario.saludo()