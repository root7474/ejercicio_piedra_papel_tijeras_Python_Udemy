from Logica.ListaOpcionesJuegoLogica import ListaOpcionesJuegoLogica

class JuegoLogica(ListaOpcionesJuegoLogica):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__puntosIA = 0
        self.__puntosUser = 0

    def setPuntosIA(self, puntosIA):
        self.__puntosIA = puntosIA

    def setPuntosUser(self, puntosUser):
        self.__puntosUser = puntosUser

    def getPuntosIA(self):
        return self.__puntosIA

    def getPuntosUser(self):
        return self.__puntosUser

    def juegoLogica(self, lista, intentos):
        condicion = False

        from Logica.Logica import Logica
        logica = Logica(self.getNombre())

        while condicion == False:
            logica.logica(lista, intentos)
            intentos -= 1

            if intentos == 0:
                self.setPuntosIA(logica.getContadorPuntosIA())
                self.setPuntosUser(logica.getContadorPuntosUser())

                if self.getPuntosUser() > self.getPuntosIA():
                    print(f"\n{self.getNombre()} has ganado :D!!!")
                elif self.getPuntosUser() < self.getPuntosIA():
                    print("Ha ganado la IA ;(")
                else:
                    print("Ha habido un empate")
                condicion = True
