def decorador(func):
    def nueva_funcion(self, parametro1,parametro2):
        print( " Perro dice : ")
        func(self, parametro1, parametro2)

    return nueva_funcion

class perro(object):
    def __init__(self, nombre):
        self.nombre = nombre

    @decorador
    def saluda(self, mensaje,nombre):
        self.mensaje = mensaje
        print( mensaje)
        print(nombre)
        print(" Guau! ")
    
    @decorador
    def ordeno(self, orden, pedo):
        self.orden = orden
        print(orden)
        print(pedo)
        print("la pata, la pata afgsad!! guau!!")

    

maty= perro("maty")
maty.saluda("uso puppy linux!!", "maty")
maty.ordeno("doy la pata", "firulais")

        
