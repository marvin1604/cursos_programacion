class Casilla_de_votacion:

    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais          = pais
        self.__region        = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError("la region", region, "no esw valida en ", self.__pais)

casilla= Casilla_de_votacion(123,["ciudad de mexico", "morelos"])
print("pais actual: ", casilla.region)
casilla.region = "ciudad de mexico"
print("pais actual: ", casilla.region)
casilla.region = "morelos"
print("pais actual: ", casilla.region)