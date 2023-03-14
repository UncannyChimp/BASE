from modulos import saludo, mascotas
from camelcase import CamelCase

print(mascotas)
saludo("Guapo")

c = CamelCase()
s = 'Esta oracion necesita calemcase'

camelCase = c.hump(s)
print(camelCase)