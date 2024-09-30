class Piece:
    
    #Despues de una pequeña charla con el sabio de la montaña llegue quedamos de acuerdo en que los mas optimo seria hace que type sea una variable
    #compartida ayudando a que los cambios sean mas simples para el codigo 
    __type__ = None
   
   #Esta funcion inicia a las piezas
    def __init__(self, color):
        self.__color__ = color
        
    #Preguntandole al sabio de la montana llegue a la conclucion que esto es para que cada pieza tenga su representacion en el tablero
    def __str__(self):
        if self.__color__ == "WHITE":
            return self.__white_str__
        else:
            return self.__black_str__        

    #Funciones creada por el sabio de la montana
    def permited_move_diagonal(self, from_row, from_col, to_row, to_col, board):
        return abs(to_row - from_row) == abs(to_col - from_col)

    #Funciones creada por el sabio de la montana    
    def permited_move_orthogonal(self, from_row, from_col, to_row, to_col, board):
        if to_row == from_row and to_col != from_col:
            return True
        elif to_col == from_col and to_row != from_row:
            return True




