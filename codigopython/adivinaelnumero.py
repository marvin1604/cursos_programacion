from random import random
import random
def run():
    contador=0
    print(" Bienvenido al juego: adivina el numero que piensa la computadora")
    num_aleatorio=random.randint(1,100)
    num_elegido = int(input("Ahora, Elige un numero del 1 al 100: "))

    while num_elegido != num_aleatorio:
        if num_elegido<num_aleatorio:
            print("ingresa un numero mas grande")
            contador +=1
        if num_elegido>num_aleatorio:
            print("ingresa un numero mas pequeño")
            contador +=1
        num_elegido = int(input("ingresa otro numero: "))
    print("Ganaste el juego!!!!!")
    print("numero de intentos realizados", contador)


if __name__== "__main__":
    run()
