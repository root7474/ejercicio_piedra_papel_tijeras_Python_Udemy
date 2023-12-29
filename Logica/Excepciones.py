"""
Clase "Excepciones()" en donde guardaremos las excepciones creadas por el usuario.
Esta clase contiene las siguientes propiedades:
    - Dos atributos privados
    - Un constructor en donde inicializamos a los atributos de la clase
    - Dos métodos get que retornarán los valores de los atributos de esta clase
    - Dos funciones que mostrarán las excepciones creadas por el usuario
"""
class Excepciones():
    """
     Creamos un constructor para esta clase que contiene lo siguiente:
        - Un parámetro "self"
        - Dos atributos privados
    """
    def __init__(self):
        self.__userData = 0 # Creamos un atributo privado "__userData" y lo inicializamos en cero
        self.__userName = None # Creamos un atributo privado "__userName" y le pasamos un valor nulo

    # Creamos los métodos get que nos devolverán el valor que reciban los atributos de esta clase
    # A estos métodos les pasamos el parámetro "self"
    def getUserData(self):
        return self.__userData

    def getUserName(self):
        return self.__userName

    """
    Función "excepcionOpciones() que permite crear una excepción si no se ingresan valores enteros.
    Esta función contiene lo siguiente:
        - Un parámetro "self" que nos permite llamar a los atributos de esta clase
        - Un parámetro "mensaje" que recibe un valor de string
        - Una variable "condicion" que servirá como condicional para el bucle de esta función
    """
    def excepcionOpciones(self, mensaje: str):
        condicion = False # Inicializamos a "condición" en "False"

        # Mientras que "condicion" sea igual a "False", haremos lo siguiente:
        while condicion == False:
            # Creamos dos bloques try... except
            try:
                # Este bloque se ejecutará si no existen excepciones durante la ejecución del programa
                self.__userData = int(input(mensaje)) # A "__userData" le pasamos el valor de "mensaje y un valor entero ingresado por el usuario
                condicion = True # Le pasamos un valor de "True" a "condición" y finalizamos la ejecución del ciclo
            except ValueError:
                # Si no se ingresan números enteros
                print("Error!!!... Solo debes ingresar números enteros") # Imprimimos un mensaje de error

        return self.getUserData() # Retornamos el valor actual del método "getUserData()"

    """
    Función "excepcionNombre() que permite crear una excepción si no se ingresa un nombre de usuario correcto.
    Esta función contiene lo siguiente:
        - Un parámetro "self" que nos permite llamar a los atributos de esta clase
        - Un parámetro "mensaje" que recibe un valor de string
        - Una variable "condicion" que servirá como condicional para el bucle de esta función
    """
    def excepcionNombre(self, mensaje: str):
        condicion = False # Inicializamos a "condición" en "False"

        # Mientras que "condicion" sea igual a "False", haremos lo siguiente:
        while condicion == False:
            self.__userName = input(mensaje) # A "__userName" le pasamos el valor de "mensaje y un nombre ingresado por el usuario

            if len(self.getUserName()) < 3:
                # Si la longitud del nombre es menor a 3
                print("Error!!!... La extensión del nombre debe ser mayor a 3 caracteres") # Imprimimos un mensaje de error
            else:
                # Si la longitud del nombre es mayor a 3
                condicion = True # Le pasamos un valor de "True" a "condicion" y finalizamos la ejecución del ciclo

        return self.getUserName() # Retornamos el valor actual del método "getUserName()"
