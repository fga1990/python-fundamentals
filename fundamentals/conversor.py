pesos = input("¿Cuántos pesos colombianos tienes?: ")
pesos = float(pesos)

valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")

pesos_mexicanos = round((float(input("Cuántos pesos méxicanos tienes?: ")) / valor_dolar), 2)
print("Tienes $" + str(pesos_mexicanos) + " dólares")
