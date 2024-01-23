# Ejercicio 12
barras_viejas = int(input('¿Cuántas barras no son frescas?: '))
barras_frescas = int(input('¿Cuántas barras SÍ que son frescas?: '))
descuento = 0.6
barra_con_descuento = 0.75 - (0.75 * 0.6)
barra = 0.75
print('El precio es: ' + str(round((barras_viejas * barra_con_descuento) + (barras_frescas * barra), 2)) + '€')