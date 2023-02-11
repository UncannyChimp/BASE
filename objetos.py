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

usuario.saludo()
usuario.nombre = "Chanchito"
usuario.saludo()

#-----------Eliminar cosas-------------------
# del usuario.nombre 
# usuario.saludo()
# del usuario

admin = Admin("Super", "Admin")
admin.saludo()
admin.superSaludo()