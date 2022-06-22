menu = """
Bienvenido al conversor de monedas💰💰
1- soles
2. pesos colombianos
3.peso mexicanos
Elige la opcion: """

opcion=input(menu)
if opcion=="1":
    soles = float(input("ingrese la cantidad de soles a cambiar: "))
    valor_dolar = 3.70
    dolares = soles/valor_dolar
    dolares= str(round(dolares, 3))
    print("tienes $"+ dolares+ " dolares")

elif opcion=="2":
    soles = float(input("ingrese la cantidad de pesos colombianos a cambiar: "))
    valor_dolar = 3875
    dolares = soles/valor_dolar
    dolares= str(round(dolares, 3))
    print("tienes $"+ dolares+ " dolares")
elif opcion=="3":
    soles = float(input("ingrese la cantidad de pesos argentinos a cambiar: "))
    valor_dolar = 65
    dolares = soles/valor_dolar
    dolares= str(round(dolares, 3))
    print("tienes $"+ dolares+ " dolares")
else:
    print("ingrese una opcion valida por favor")

