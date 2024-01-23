# Ejercicio 11
inversión = float(input("Introduce la inversión inicial: "))
interés = 0.04
balance1 = inversión * (1 + interés)
print("Balance tras el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interés)
print("Balance tras el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interés)
print("Balance tras el tercer año:" + str(round(balance3, 2)))