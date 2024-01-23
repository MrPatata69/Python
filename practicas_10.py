# Ejercicio 10
num_payasos = int(input('¿Cuántos payasos se van a enviar?'))
num_muñecas = int(input('¿Cuántas muñecas se van a enviar?'))
peso_payasos = 112 * num_payasos
peso_muñecas = 75 * num_muñecas
peso_del_paquete = peso_payasos + peso_muñecas
print('El peso total del paquete es: ', str(peso_del_paquete), 'gramos')