# Importamos a la clase "ListaOpcionesJuegoLogica()" del módulo "ListaOpcionesJuegoLogica"
from Logica.ListaOpcionesJuegoLogica import ListaOpcionesJuegoLogica

"""
Clase "JuegoLogica()" en donde iniciaremos con la lógica del juego.
Esta clase hereda de la clase "ListaOpcionesJuegoLogica()" y contiene las siguientes propiedades:
    - Dos atributos privados
    - Un constructor en donde inicializamos a los atributo de la clase
    - Dos métodos set que reciben un acumulado de puntos
    - Dos método get que retornarán el valor de los atributos de esta clase
    - Una función que contendrá toda la lógica del juego
"""
class JuegoLogica(ListaOpcionesJuegoLogica):
    """
    Creamos un constructor para esta clase.
    Este constructor hereda los atributos del constructor de la clase padre y contiene lo siguiente:
        - Dos parámetros "self" y "nombre" de tipo string que recibe el nombre del usuario
        - Dos atributos privados
    """
    def __init__(self, nombre: str):
        super().__init__(nombre) # Llamamos a todos los atributos del contructor de la clase padre
        self.__puntosIA = 0 # Creamos un atributo privado "__puntosIA" y le pasamos un valor de cero
        self.__puntosUser = 0 # Creamos un atributo privado "__puntosUser" y le pasamos un valor de cero

    # Creamos los métodos set que reciben como parámetros "self" y los puntos tanto del usuario como de la IA
    def setPuntosIA(self, puntosIA: int):
        self.__puntosIA = puntosIA # Al atributo "__puntosIA" le asignamos el valor del parámetro "puntosIA"

    def setPuntosUser(self, puntosUser: int):
        self.__puntosUser = puntosUser # Al atributo "__puntosUser" le asignamos el valor del parámetro "puntosUser"

    # Creamos los métodos get que nos devolverán el valor que reciban los atributos de esta clase
    # A estos métodos les pasamos el parámetro "self"
    def getPuntosIA(self):
        return self.__puntosIA

    def getPuntosUser(self):
        return self.__puntosUser

    """
    Función "juegoLogica()" en donde creamos la lógica del juego.
    Esta función contiene lo siguiente:
        - Un parámetro "self" que nos permite llamar a los atributos de esta clase
        - Un parámetro "lista" de tipo list que recibe una lista de opciones
        - Un parámetro "intentos" de tipo entero que recibe una cantidad de intentos
        - Una instancia de la clase "Logica()" del módulo "Logica"
        - Una variable "condicion" que servirá como condicional para el bucle de esta función
    """
    def juegoLogica(self, lista: list, intentos: int):
        from Logica.Logica import Logica # Importamos a la clase "Logica()"

        condicion = False # Inicializamos a "condición" en "False"
        logica = Logica(self.getNombre()) # Creamos una variable "logica" e instanciamos a la clase "Logica()"

        # Mientras que "condicion" sea igual a "False", haremos lo siguiente:
        while condicion == False:
            # Hacemos una llamamos a la función "logica()" y le pasamos los valores de "lista" y de "intentos"
            logica.logica(lista, intentos)
            intentos -= 1 # En cada ejecución le restamos -1 a "intentos"

            if intentos == 0:
                # Si "intentos" es igual a 0
                # Enviamos el valor que retornev los métodos "getContadorPuntosIA()" y"getContadorPuntosUser()"
                # De la clase "Logica()" a los métodos "setPuntosIA()" y "setPuntosUser()" de esta clase
                self.setPuntosIA(logica.getContadorPuntosIA())
                self.setPuntosUser(logica.getContadorPuntosUser())

                if self.getPuntosUser() > self.getPuntosIA():
                    # Si la cantidad de puntos del usuario es mayor a la cantidad de puntos de la IA
                    print(f"\n{self.getNombre()} has ganado :D!!!") # Imprimimos este mensaje
                elif self.getPuntosUser() < self.getPuntosIA():
                    # Si la cantidad de puntos de la IA es mayor a la cantidad de puntos del usuario
                    print("Ha ganado la IA ;(") # Imprimimos este mensaje
                else:
                    print("Ha habido un empate") # Si ambas cantidades son iguales, imprimimos este mensaje
                condicion = True # Le pasamos un valor de "True" a "condición" y finalizamos la ejecución del ciclo
