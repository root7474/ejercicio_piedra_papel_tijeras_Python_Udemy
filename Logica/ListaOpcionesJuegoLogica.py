from Logica.Opciones import Opciones

class ListaOpcionesJuegoLogica(Opciones):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__lista = None

    def setLista(self, lista):
        self.__lista = lista

    def getLista(self):
        return self.__lista

    def listaOpciones(self, intentos):
        from Logica.JuegoLogica import JuegoLogica

        lista = ["Piedra", "Papel", "Tijeras"]
        juegoLogica = JuegoLogica(self.getNombre())

        self.setLista(lista)
        juegoLogica.juegoLogica(self.getLista(), intentos)
