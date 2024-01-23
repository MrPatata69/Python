# Ejercicio 8
n = int(input('Introduce un número entero (dividendo): '))
m = int(input('Introduce otro número entero (divisor): '))
c = n / m
r = str(int(n) % int(m))
print(str(n), 'entre ', str(m), 'da un cociente de: ', str(c), 'y un resto de: ', str(r))