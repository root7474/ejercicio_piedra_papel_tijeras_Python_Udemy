import random
import sys

from Logica.ListaOpcionesJuegoLogica import ListaOpcionesJuegoLogica

class Logica(ListaOpcionesJuegoLogica):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__contadorPuntosIA = 0
        self.__contadorPuntosUser = 0

    def setContadorPuntosIA(self, contadorPuntosIA):
        self.__contadorPuntosIA = contadorPuntosIA

    def setContadorPuntosUser(self, contadorPuntosUser):
        self.__contadorPuntosUser = contadorPuntosUser

    def getContadorPuntosIA(self):
        return self.__contadorPuntosIA

    def getContadorPuntosUser(self):
        return self.__contadorPuntosUser

    def logica(self, lista, intentos):
        opcionIA = lista
        opcionIA = random.choice(opcionIA)
        opcionUserString = None
        condicion = False

        print(f"Faltan {intentos} intentos")

        while condicion == False:
            print(f"\n{self.getNombre()} digita una opción:\n")

            for i in range(len(lista)): print(f"{i + 1}.) {lista[i]}")
            print("0.) Salir")
            opcionUserInt = self.excepcionOpciones("\nOpción: ")

            match(opcionUserInt):
                case 1:
                    opcionUserString = lista[0]
                    condicion = True
                case 2:
                    opcionUserString = lista[1]
                    condicion = True
                case 3:
                    opcionUserString = lista[2]
                    condicion = True
                case 0:
                    print("Hasta pronto...")
                    sys.exit(0)
                case default:
                    print("Error!!!... Opción incorrecta")

        if opcionUserString == "Piedra" and opcionIA == "Tijeras":
            self.__contadorPuntosUser += 1
            self.setContadorPuntosUser(self.__contadorPuntosUser)
            print(f"{self.getNombre()}: {opcionUserString} vs IA: {opcionIA}\n"
                  f"{self.getNombre()} has ganado +1 puntos.\n")
        elif opcionUserString == "Papel" and opcionIA == "Piedra":
            self.__contadorPuntosUser += 1
            self.setContadorPuntosUser(self.__contadorPuntosUser)
            print(f"{self.getNombre()}: {opcionUserString} vs IA: {opcionIA}\n"
                  f"{self.getNombre()} has ganado +1 puntos.\n")
        elif opcionUserString == "Tijeras" and opcionIA == "Papel":
            self.__contadorPuntosUser += 1
            self.setContadorPuntosUser(self.__contadorPuntosUser)
            print(f"{self.getNombre()}: {opcionUserString} vs IA: {opcionIA}\n"
                  f"{self.getNombre()} has ganado +1 puntos.\n")
        elif opcionUserString == opcionIA:
            print(f"{self.getNombre()}: {opcionUserString} vs IA: {opcionIA}")
            print("Ha habido un empate\n")
        else:
            self.__contadorPuntosIA += 1
            self.setContadorPuntosIA(self.__contadorPuntosIA)
            print(f"{self.getNombre()}: {opcionUserString} vs IA: {opcionIA}\n"
                  "LA IA ha ganado +1 puntos.\n")

        print(f"{self.getNombre()}: {self.getContadorPuntosUser()} vs IA: {self.getContadorPuntosIA()}")
