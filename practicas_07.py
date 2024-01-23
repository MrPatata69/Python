# Ejercicio 7
kg = float(input('¿Cuánto pesas en kg?: '))
estatura = float(input('¿Cuánto mides en metros?: '))
imc = (kg / (estatura ** 2))
print('Tu índice de masa corporal es: ', str(round(imc, 2)))