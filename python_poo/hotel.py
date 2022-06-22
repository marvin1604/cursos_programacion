class Hotel():

    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

    def añadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes

hotel =Hotel(50,20)
print("numero maximo de huespedes: ", hotel.numero_maximo_de_huespedes)
print("lugares de estacionamientos: ", hotel.lugares_de_estacionamiento)

hotel.añadir_huespedes(10)
hotel.checkout(1)
hotel.ocupacion_total()
print(hotel.huespedes)
