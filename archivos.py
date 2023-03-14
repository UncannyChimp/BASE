# c = open('chanchito.txt')
# print(c.read())
# print(c.readline())

# for x in c:
#     print(x)

# c = open('chanchito.txt', 'a')

# c.write('\nAgregaremos una nueva linea a nuestro archivo')

# c.close()

# x = open('chanchito.txt')
# print(x.read())

## Si usamos : c = open('chanchito.txt', 'w')
# significara que estamos reescribiendo todo en vez de solo agregando

import os

if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
else:
    print('El archivo no existe')

os.rmdir('micarpeta')