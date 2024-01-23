# Variables

my_string_variable = 'Esto es mi variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print('Este es el valor de :', my_bool_variable)

# Tipo 'NoneType'
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable)))

# Algunas funciones del sistema

# Cuenta los carácteres
print(len(my_int_to_str_variable))
print(len(my_string_variable))

# Variables en una sola línea. No abusar de esta sintaxis
name, surname, alias, age = 'Lucas', 'Sánchez', 'LUCAS 540', 14
print('Mi nombre es:', name, surname, 'Y mi alias y mi edad son:', alias, age)

# Inputs
'''
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')

print(name)
print(age)
'''

# Cambiamos su tipo
name = 14
age = 'Lucas'
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = 'Mi dirección'
address = 32
print(type(address))