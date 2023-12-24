from Logica.Excepciones import Excepciones

class Opciones(Excepciones):
    def __init__(self, nombre):
        super().__init__()
        self.__nombre = nombre
        self.__opcion = 0

    def setOpcion(self, opcion):
        self.__opcion = opcion

    def getNombre(self):
        return self.__nombre

    def getOpcion(self):
        return self.__opcion

    def menu(self):
        from Logica.ListaOpcionesJuegoLogica import ListaOpcionesJuegoLogica

        condicion = False

        listaOpciones = ListaOpcionesJuegoLogica(self.getNombre())

        while condicion == False:
            opcion = self.excepcionOpciones(f"{self.getNombre()} digita una opción:\n"
                                      "\n1.) Continuar con el juego"
                                      "\n2.) Salir del juego"
                                      "\n\nOpción: ")

            self.setOpcion(opcion)

            if self.getOpcion() == 1:
                intentos = self.excepcionOpciones(f"{self.getNombre()} digita una cantidad de intentos: ")
                listaOpciones.listaOpciones(intentos)
            elif self.getOpcion() == 2:
                print("Hasta pronto...")
                condicion = True
            else:
                print("Error!!!... Opción incorrecta")
