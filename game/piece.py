class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__type__ = None

#Preguntandole al sabio de la montana llegue a la conclucion que esto es para que cada pieza tenga su representacion en el tablero
    def __str__(self):
        raise NotImplementedError("Subclasses must implement this method.")
        
