# Operadores

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print (2 ** 3)
print (2 ** 3 + 3 - 7 / 1 // 4)

# Siempre dara un dato 'int' aunque el resultado sea 'float'
print(10 // 3)

# Concatenación de cadenas de texto
print('Hola ' + 'Python ' + '¿Qué tal estás?')
print('Hola' + str(5))
print('Hola ' * 5)
print('Hola ' * (2 ** 5))

my_float = 2.5 * 2
print('Hola' * int(my_float))

# Operadores comparativos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)
print(3 > 4 > 2)

# Separación
print('(Esto es un separador para la consola)')
# Separación

print('Hola' > 'Python')
print('Hola' < 'Python')
print('aaaa' >= 'abaa') # Ordenación alfabética por ASCII
print(len('aaaa') >= len('abaa')) #Comparación por carácteres
print('Hola' <= 'Python')
print('Hola' == 'Python')
print('Hola' != 'Python')

# Operadores lógicos

print(3 > 4 and 'Hola' > 'Python')
print(3 > 4 or 'Hola' > 'Python')
print(3 < 4 or 'Hola' < 'Python')
print(3 < 4 or 'Hola' > 'Python')
print(3 < 4 or ('Hola' > 'Python' and 4 == 4))
print(not(3 > 4)) # Es 'False' pero al ponerle 'not' se convierte en 'True'
