menu = """
Bienvenidos al conversor de monedas

1.- Pesos colombianos
2.- Pesos Argentinos
3.- Pesos Mexicanos

Elegir una opción:
"""

opcion = int(input(menu))

if opcion == 1:
    valor_dolar = 3875
    pesos = round((float(input("Cuántos pesos colombianos tienes?: ")) / valor_dolar), 2)
    print("Tienes $" + str(pesos) + " dólares")
elif opcion == 2:
    valor_dolar = 3875
    pesos = round((float(input("Cuántos pesos argentinos tienes?: ")) / valor_dolar), 2)
    print("Tienes $" + str(pesos) + " dólares")
elif opcion == 3:
    valor_dolar = 23
    pesos = round((float(input("Cuántos pesos mexicanos tienes?: ")) / valor_dolar), 2)
    print("Tienes $" + str(pesos) + " dólares")