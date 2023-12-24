class Excepciones():
    def __init__(self):
        self.__userData = 0
        self.__userName = None

    def getUserData(self):
        return self.__userData

    def getUserName(self):
        return self.__userName

    def excepcionOpciones(self, mensaje):
        condicion = False

        while condicion == False:
            try:
                self.__userData = int(input(mensaje))
                condicion = True
            except ValueError:
                print("Error!!!... Solo debes ingresar números enteros")

        return self.getUserData()

    def excepcionNombre(self, mensaje):
        condicion = False

        while condicion == False:
            self.__userName = input(mensaje)

            if len(self.getUserName()) < 3:
                print("Error!!!... La extensión del nombre debe ser mayor a 3 caracteres")
            else:
                condicion = True

        return self.getUserName()
