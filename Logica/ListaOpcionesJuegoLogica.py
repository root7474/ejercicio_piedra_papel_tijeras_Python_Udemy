from Logica.Opciones import Opciones # Importamos a la clase "Opciones()" del módulo "Opciones"

"""
Clase "ListaOpcionesJuegoLogica()" en donde guardaremos una lista de opciones para la lógica del juego.
Esta clase hereda de la clase "Opciones()" y contiene las siguientes propiedades:
    - Un atributo privado
    - Un constructor en donde inicializamos al atributo de la clase
    - Un método set que recibe una lista de opciones
    - Un método get que retornará el valor del atributo de esta clase
    - Una función que contendrá una lista de opciones
"""
class ListaOpcionesJuegoLogica(Opciones):
    """
    Creamos un constructor para esta clase.
    Este constructor hereda los atributos del constructor de la clase padre y contiene lo siguiente:
        - Dos parámetros "self" y "nombre" de tipo string que recibe el nombre del usuario
        - Un atributos privado
    """
    def __init__(self, nombre: str):
        super().__init__(nombre) # Llamamos a todos los atributos del contructor de la clase padre
        self.__lista = None # Creamos un atributo privado "__lista" y le pasamos un valor nulo

    # Creamos un método set y le pasamos "self" y "lista" de tipo list
    def setLista(self, lista: list):
        self.__lista = lista # Al atributo "__lista" le asignamos el valor del parámetro "lista"

    # Creamos un método get que retornará el valor del atributo "__lista" y le pasamos el parámetro "self"
    def getLista(self):
        return self.__lista

    """
    Función "listaOpciones()" que guarda una lista de opciones de piedra, papel o tijeras.
    Esta función contiene lo siguiente:
        - Un parámetro "self" que nos permite llamar a los atributos de esta clase
        - Un parámetro "intentos" de tipo entero que recibe una cantidad de intentos
        - Una instancia de la clase "JuegoLogica()" del módulo "JuegoLogica"
    """
    def listaOpciones(self, intentos: int):
        from Logica.JuegoLogica import JuegoLogica # Importamos a la clase "JuegoLogica()"

        lista = ["Piedra", "Papel", "Tijeras"] # Dentro de "lista", guardamos las opciones de piedra, papel o tijeras
        juegoLogica = JuegoLogica(self.getNombre()) # Creamos una variable "juegoLogica" e instanciamos a la clase "JuegoLogica()"

        self.setLista(lista) # Hacemos una llamado al método "setLista()" y le pasamos el valor de "lista"
        juegoLogica.juegoLogica(self.getLista(), intentos) # Llamamos a la función "juegoLogica()" y le pasamos el valor de "getLista()" y de "intentos"
