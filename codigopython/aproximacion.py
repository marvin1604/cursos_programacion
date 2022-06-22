from time import time
#numero al que se le calculara la raiz cuadrada
objetivo = int(input('Escoge un numero: '))
#margen de error para encontrar esa raiz cuadrada
epsilon = 0.01
# valor que se ira sumando secuencialemnte hasta encontrar la raiz cuadrada
paso = epsilon**2
#se comenzara a buscar la raiz cuadrada desde 0.0 en adelante
respuesta = 0.0

#calculo del tiempo que se demora al proceso
tiempo_inicio = time()

#mientras que la respuesta al cuadrado no sea igual al objetivo( con un margen de error de 0.01, es decir epsilon), este while se seguira ejecutando
#respuesta<=objetivo: codigo defensivo; si respuesta es mayor a objetico, el while seguira infinitamente, y nunca enconrara a la raiz cuadrada
# ( la raiz cuadrada nunca sera mas grande que el objetivo)
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

tiempo_total = time() - tiempo_inicio

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada del objetivo')
    print(f'Tardo {tiempo_total} segundos')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    print(f'Tardo {tiempo_total} segundos')