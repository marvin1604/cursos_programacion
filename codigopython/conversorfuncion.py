def conversor(tipo_pesos, valor_dolar):
    soles = input("ingrese la cantidad de "+ tipo_pesos + " a cambiar: ")
    soles = float(soles)
    dolares = soles/valor_dolar
    dolares= str(round(dolares, 3))
    print("tienes $"+ dolares+ " dolares")


menu = """
Bienvenido al conversor de monedas💰💰
1- soles
2. pesos colombianos
3.peso argentinos
Elige la opcion: """

opcion=input(menu)
if opcion=="1":
    conversor("soles",3.70)
elif opcion=="2":
    conversor("pesos colombianos",3875)
elif opcion=="3":
    conversor(" pesos argentinos",65)
else:
    print("ingrese una opcion valida por favor")

