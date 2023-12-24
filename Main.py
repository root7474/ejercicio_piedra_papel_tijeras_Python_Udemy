import sys
from Logica.Opciones import Opciones
from Logica.Excepciones import Excepciones

def main():
    try:
        excepciones = Excepciones()
        nombre = excepciones.excepcionNombre("Bienvenido...\nDigita tu nombre: ")
        opciones = Opciones(nombre)
        opciones.menu()
    except EOFError:
        print("Hasta pronto...")
        sys.exit(0)

if __name__ == "__main__":
    main()
