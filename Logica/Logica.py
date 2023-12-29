# Importamos los módulos a usar
import random
import sys

# Importamos a la clase "ListaOpcionesJuegoLogica()" del módulo "ListaOpcionesJuegoLogica"
from Logica.ListaOpcionesJuegoLogica import ListaOpcionesJuegoLogica

"""
Clase "Logica()" en donde crearémos la lógica de puntos del usuario y de la IA.
Esta clase hereda de la clase "ListaOpcionesJuegoLogica()" y contiene las siguientes propiedades:
    - Dos atributos privados
    - Un constructor en donde inicializamos a los atributos de la clase
    - Dos métodos set que reciben un acumulado de puntos
    - Dos método get que retornarán el valor de los atributos de esta clase
    - Una función que contendrá toda la lógica de los puntos del juego
"""
class Logica(ListaOpcionesJuegoLogica):
    """
    Creamos un constructor para esta clase.
    Este constructor hereda los atributos del constructor de la clase padre y contiene lo siguiente:
        - Dos parámetros "self" y "nombre" de tipo string que recibe el nombre del usuario
        - Dos atributos privados
    """
    def __init__(self, nombre: str):
        super().__init__(nombre) # Llamamos a todos los atributos del contructor de la clase padre
        self.__contadorPuntosIA = 0 # Creamos un atributo privado "__contadorPuntosIA" y le pasamos un valor de cero
        self.__contadorPuntosUser = 0 # Creamos un atributo privado "__contadorPuntosUser" y le pasamos un valor de cero

    # Creamos los métodos set que reciben como parámetros "self" y un contador de puntos tanto del usuario como de la IA
    def setContadorPuntosIA(self, contadorPuntosIA: int):
        self.__contadorPuntosIA = contadorPuntosIA # Al atributo "__contadorPuntosIA" le asignamos el valor del parámetro "__contadorPuntosIA"

    def setContadorPuntosUser(self, contadorPuntosUser: int):
        self.__contadorPuntosUser = contadorPuntosUser # Al atributo "__contadorPuntosUser" le asignamos el valor del parámetro "__contadorPuntosUser"

    # Creamos los métodos get que nos devolverán el valor que reciban los atributos de esta clase
    # A estos métodos les pasamos el parámetro "self"
    def getContadorPuntosIA(self):
        return self.__contadorPuntosIA

    def getContadorPuntosUser(self):
        return self.__contadorPuntosUser

    """
    Función "logica()" en donde crearémos un acumulado de puntos tanto del usuario como de la IA.
    Esta función contiene lo siguiente:
        - Un parámetro "self" que nos permite llamar a los atributos de esta clase
        - Un parámetro "lista" de tipo list que recibe una lista de opciones
        - Un parámetro "intentos" de tipo entero que recibe una cantidad de intentos
        - Una variable "opcionIA" que recibe una lista de opciones para la IA
        - Una variable "opcionUserString" a la que le asignamos un valor de la lista de opciones de "lista"
        - Una variable "condicion" que servirá como condicional para el bucle de esta función
        - Una variable "opcionUserInt" que recibe un valor entero
    """
    def logica(self, lista: list, intentos: int):
        opcionIA = lista # A "opcionIA" le pasamos el valor de "lista"
        opcionIA = random.choice(opcionIA) # A través de "random.choice()" le permitimos a la IA seleccionar una opción aleatoria
        opcionUserString = None # A "opcionUserString" le pasamos un valor nulo
        condicion = False # Inicializamos a "condición" en "False"

        print(f"Faltan {intentos} intentos") # Imprimimos el número de intentos restantes

        # Mientras que "condicion" sea igual a "False", haremos lo siguiente:
        while condicion == False:
            print(f"\n{self.getNombre()} digita una opción:\n") # Pedimos que se ingrese una opción

            # Enumeramos todos los elementos de la lista y los imprimimos
            for i in range(len(lista)): print(f"{i + 1}.) {lista[i]}")

            print("0.) Salir") # Agregamos la opción de salir

            # Hacemos una llamada a la función "excepcionOpciones()" y le pasamos un string
            opcionUserInt = self.excepcionOpciones("\nOpción: ") # Dentro de "opcionUserInt" guardamos el valor que retorne la función

            # Mediante la función "match()" creamos una casuistica de las opciones que ingrese el usuario
            match(opcionUserInt):
                case 1:
                    # Para el caso de la opción 1
                    opcionUserString = lista[0] # A "opcionUserString" le asignamos el primer valor de la lista
                    condicion = True # Le pasamos un valor de "True" a "condicion" y finalizamos la ejecución del ciclo
                case 2:
                    # Para el caso de la opción 2
                    opcionUserString = lista[1] # A "opcionUserString" le asignamos el segundo valor de la lista
                    condicion = True # Le pasamos un valor de "True" a "condicion" y finalizamos la ejecución del ciclo
                case 3:
                    # Para el caso de la opción 3
                    opcionUserString = lista[2] # A "opcionUserString" le asignamos el tercer valor de la lista
                    condicion = True # Le pasamos un valor de "True" a "condicion" y finalizamos la ejecución del ciclo
                case 0:
                    # Para el caso de la opción 0
                    print("Hasta pronto...") # Imprimimos un mensaje de despedida
                    sys.exit(0) # Con  la función "exit()" del módulo "sys", le ordenamos al programa que finalice su ejecución
                case default:
                    print("Error!!!... Opción incorrecta") # Creamos un caso por defecto si se ingresa una opción incorrecta

        if opcionUserString == "Piedra" and opcionIA == "Tijeras":
            # Si la opción que ha elegido el usuario es igual a "Piedra" y la opción de la IA es igual a "Tijeras"
            self.__contadorPuntosUser += 1 # Incrementamos en 1 el valor de "__contadorPuntosUser"
            self.setContadorPuntosUser(self.__contadorPuntosUser) # Enviamos el valor de "__contadorPuntosUser" al método "setContadorPuntosUser()"

            # Le informamos al usuario la opción que ha elegido y los puntos que ha ganado
            print(f"{self.getNombre()}: {opcionUserString} vs IA: {opcionIA}\n"
                  f"{self.getNombre()} has ganado +1 puntos.\n")
        elif opcionUserString == "Papel" and opcionIA == "Piedra":
            # Si la opción que ha elegido el usuario es igual a "Papel" y la opción de la IA es igual a "Piedra"
            self.__contadorPuntosUser += 1 # Incrementamos en 1 el valor de "__contadorPuntosUser"
            self.setContadorPuntosUser(self.__contadorPuntosUser) # Enviamos el valor de "__contadorPuntosUser" al método "setContadorPuntosUser()"

            # Le informamos al usuario la opción que ha elegido y los puntos que ha ganado
            print(f"{self.getNombre()}: {opcionUserString} vs IA: {opcionIA}\n"
                  f"{self.getNombre()} has ganado +1 puntos.\n")
        elif opcionUserString == "Tijeras" and opcionIA == "Papel":
            # Si la opción que ha elegido el usuario es igual a "Tijeras" y la opción de la IA es igual a "Papel"
            self.__contadorPuntosUser += 1 # Incrementamos en 1 el valor de "__contadorPuntosUser"
            self.setContadorPuntosUser(self.__contadorPuntosUser) # Enviamos el valor de "__contadorPuntosUser" al método "setContadorPuntosUser()"

            # Le informamos al usuario la opción que ha elegido y los puntos que ha ganado
            print(f"{self.getNombre()}: {opcionUserString} vs IA: {opcionIA}\n"
                  f"{self.getNombre()} has ganado +1 puntos.\n")
        elif opcionUserString == opcionIA:
            # Si la opción que ha elegido el usuario es igual a la opción generada por la IA
            # Imprimimos las opción elegida por el usuario y la opción generada por la IA
            print(f"{self.getNombre()}: {opcionUserString} vs IA: {opcionIA}")
            print("Ha habido un empate\n") # Despúes imprimimos un mensaje de empate
        else:
            # Si el usuario ingresa una opción que no le permita aumentar puntos y tampoco generar un empate
            self.__contadorPuntosIA += 1 # Aumentamos los puntos de la IA en 1
            self.setContadorPuntosIA(self.__contadorPuntosIA) # Enviamos el valor de "__contadorPuntosIA" al método "setContadorPuntosIA()"

            # Le informamos al usuario la opción que ha elegido y los puntos que ha ganado la IA
            print(f"{self.getNombre()}: {opcionUserString} vs IA: {opcionIA}\n"
                  "LA IA ha ganado +1 puntos.\n")

        # Imprimimos los puntos acumulados tanto del usuario como de la IA
        print(f"{self.getNombre()}: {self.getContadorPuntosUser()} vs IA: {self.getContadorPuntosIA()}")
