import sys # Importamos al módulo "sys"

# Importamos a las clases a usar
from Logica.Opciones import Opciones
from Logica.Excepciones import Excepciones

"""
Función "main()" que permite la ejecución del programa.
esta función contiene lo siguiente:
    - Dos instancias de las clases a usar
    - Dos llamadas a las funciones de las clases a usar
"""
def main():
    # Creamos dos bloques try... except
    try:
        # Este bloque se ejecutará si no existen excepciones durante la ejecución del programa
        excepciones = Excepciones() # Creamos una variable "excepciones" e instanciamos a la clase "Excepciones()"
        nombre = excepciones.excepcionNombre("Bienvenido...\nDigita tu nombre: ") # Creamos una variable "nombre" y llamamos a la función "excepcionNombre()"
        opciones = Opciones(nombre) # Creamos una variable "opciones" e instanciamos a la clase "Opciones()"
        opciones.menu() # Hacemos una llamada a la función "menu()"
    except EOFError:
        # Este bloque se ejecutará si existen excepciones durante la ejecución del programa
        print("Hasta pronto...") # Imprimimos un mensaje de despedida
        sys.exit(0) # Con  la función "exit()" del módulo "sys", le ordenamos al programa que finalice su ejecución

# A continuación le orednamos al programa que ejecute la función "main()"
if __name__ == "__main__":
    main()
