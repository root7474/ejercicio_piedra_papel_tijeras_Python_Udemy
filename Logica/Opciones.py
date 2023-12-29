from Logica.Excepciones import Excepciones # Importamos a la clase "Excepciones()" del módulo "Excepciones"

"""
Clase "Opciones()" en donde guardaremos las opciones para darle continuidad al juego.
Esta clase hereda de la clase "Excepciones()" y contiene las siguientes propiedades:
    - Dos atributos privados
    - Un constructor en donde inicializamos a los atributos de la clase
    - Un método set que recibe un valor ingresado por el usuario
    - Dos métodos get que retornarán los valores de los atributos de esta clase
    - Una función que permitirá mostrar un menú de opciones
"""
class Opciones(Excepciones):
    """
    Creamos un constructor para esta clase.
    Este constructor hereda los atributos del constructor de la clase padre y contiene lo siguiente:
        - Dos parámetros "self" y "nombre" de tipo string que recibe el nombre del usuario
        - Dos atributos privados
    """
    def __init__(self, nombre: str):
        super().__init__() # Llamamos a todos los atributos del contructor de la clase padre
        self.__nombre = nombre # Creamos un atributo privado "__nombre" y le pasamos el valor del parámetro "nombre"
        self.__opcion = 0 # Creamos un atributo privado "__opcion" y lo inicializamos en cero

    # Creamos un método set y le pasamos "self" y "opcion" de tipo entero
    def setOpcion(self, opcion: int):
        self.__opcion = opcion # Al atributo "__opcion" le asignamos el valor del parámetro "opcion"

    # Creamos los métodos get que nos devolverán el valor que reciban los atributos de esta clase
    # A estos métodos les pasamos el parámetro "self"
    def getNombre(self):
        return self.__nombre

    def getOpcion(self):
        return self.__opcion

    """
    Función "menu() que recibe una opción ingresada por el usuario.
    Esta función contiene lo siguiente:
        - Un parámetro "self" que nos permite llamar a los atributos de esta clase
        - Una variable "condicion" que servirá como condicional para el bucle de esta función
        - Una instancia de la clase "ListaOpcionesJuegoLogica()" del módulo "ListaOpcionesJuegoLogica"
        - Una variable "opcion" que recibe un valor entero
        - Una variable "intentos" que guarda el número de intentos dentro del juego
    """
    def menu(self):
        # Importamos a la clase "ListaOpcionesJuegoLogica()"
        from Logica.ListaOpcionesJuegoLogica import ListaOpcionesJuegoLogica

        condicion = False # Inicializamos a "condición" en "False"
        listaOpciones = ListaOpcionesJuegoLogica(self.getNombre()) # Creamos una variable "listaOpciones" e instanciamos a la clase "ListaOpcionesJuegoLogica()"

        # Mientras que "condicion" sea igual a "False", haremos lo siguiente:
        while condicion == False:
            # Hacemos una llamada a la función "excepcionOpciones()" y le pasamos un string
            opcion = self.excepcionOpciones(f"{self.getNombre()} digita una opción:\n"
                                            "\n1.) Continuar con el juego"
                                            "\n2.) Salir del juego"
                                            "\n\nOpción: ") # Dentro de "opcion" guardamos el valor que retorne la función

            self.setOpcion(opcion) # Hacemos una llamado al método "setOpcion()" y le pasamos el valor de "opcion"

            # Mediante la función "match()" creamos una casuistica de las opciones que ingrese el usuario
            match(self.getOpcion()):
                case 1:
                    # Si el valor que devuelve el método "getOpcion()" es igual a 1
                    # Llamamos a la función "excepcionOpciones()" y le pasamos un string
                    intentos = self.excepcionOpciones(f"{self.getNombre()} digita una cantidad de intentos: ") # Gaudamos el valor que retorn la función dentro de "intentos"

                    if intentos >= 1:
                        # Si "intentos" es mayor o igual que 1
                        listaOpciones.listaOpciones(intentos) # Llamamos a la función "listaOpciones()" y le pasamos el valor de "intentos"
                    else:
                        # Si intentos es menor que 1
                        print("Error!!!... Debes digitar una cantidad de intentos mayor que cero") # Imprimimos un mensaje de error
                case 2:
                    # Si el valor que devuelve el método "getOpcion()" es igual a 2
                    print("Hasta pronto...") # Imprimimos un mensaje de despedida
                    condicion = True # Le pasamos un valor de "True" a "condicion" y finalizamos la ejecución del programa
                case default:
                    print("Error!!!... Opción incorrecta") # Imprimimos un un error si la opción ingresada es incorrecta
