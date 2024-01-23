# Ejercicio 9
cantidad = float(input('Introduzca su cantidad a invertir: '))
interés = float(input('Introduzca su interés anual: '))
tiempo = int(input('Introduzca el número de años: '))
print("Capital final: " + str(round(cantidad * (interés / 100 + 1) ** tiempo, 2)))
