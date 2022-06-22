import random
import time

pasos=0

def busqueda_binaria(lista, comienzo, final, objetivo):
    print("buscando ", objetivo, "entre", lista[comienzo], "y" , lista[final-1] )
    
    global pasos

    if comienzo > final:
        pasos += 1
        return False

    medio=(comienzo + final) // 2
    pasos += 1

    if lista[medio] == objetivo:
        pasos += 1
        return True

    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)

    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

    
if __name__ == "__main__":
    tamano_de_lista = int(input("de que tamaño sera la lista? "))
    objetivo = int(input("que numero quieres encontrar?: "))
    comienzo = time.time()

    lista =sorted([random.randint(0,100) for i in range(tamano_de_lista) ])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print("el elemento", objetivo, "esta" if encontrado else "no esta", "en la lista")
    final=time.time()
    print("tiempo de busqueda",final-comienzo)
    print("cantidad de pasos: ", pasos)
