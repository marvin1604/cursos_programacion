import random
import time
pasos = 0
def busqueda_lineal(lista, objetivo):
    match = False
    global pasos
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
        pasos += 1
    return match

if __name__ == "__main__":
    tamano_de_lista = int(input("de que tamaño sera la lista? "))
    objetivo = int(input("que numero quieres encontrar?"))
    comienzo = time.time()

    lista =[random.randint(0,100) for i in range(tamano_de_lista) ]

    encontrado= busqueda_lineal(lista, objetivo)
    print(lista)
    print("el elemento", objetivo, "esta" if encontrado else "no esta", "en la lista")
    final=time.time()
    print("tiempo de busqueda",final-comienzo)
    print("cantidad de pasos", pasos)