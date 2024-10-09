from game.chess import Chess
from game.piece import Piece
from game.exceptions import InvalidPosition, NotPieceToMove, NotPermitedMove, NotPieceToReplace

class Cli():
 
    #Esta funcion lo que hace es uniciar todo el juego
    def __init__(self):
        self.chess = Chess()

    
    #Inicia la funcion play
    def main(self):
        self.play()


    #Pide la posicion de la pieza que queres elegir, se fija que este dentro del tablero y si esta bien te imprime en la terminal la pieza que elejiste
    def verify_move(self, chess):
        while True:
            try:
                from_row = int(input("De fila: "))
                from_col = int(input("De columna: "))
                self.chess.error_out_of_range(from_row, from_col)
                print("La pieza que elejiste es: ", chess.__board__.get_piece_to_show(from_row, from_col))
                if self.verify_color(chess, from_row, from_col):
                    return from_row, from_col
            except ValueError:
                print("Flasehaste, mete un numero")
            except InvalidPosition as e: #porque e? no se el gabi lo puso asi xd
                print(e)
                
                
    #Conjuncion de todas las funciones para poder jugar
    def play(self):
        a = "s"        
        while a == "s":
            self.chess.__board__.show_board() 
            try:
                from_row, from_col = self.verify_move(self.chess)
                to_row, to_col = self.validate_range_to()
                print(self.chess.__board__.capture_piece(from_row, from_col, to_row, to_col))
                self.chess.movement_fits(from_row, from_col,to_row,to_col) 
                self.chess.change_pawn_to_other(from_row, from_col, to_row, to_col)
                self.chess.__board__.show_board() 
                print(self.chess.show_captured_pieces())
                if self.chess.verify_winner() is not False:
                    print(self.chess.verify_winner())
                    a = "n"
                    break
                a = input("Quieres seguir jugando? (s/n): ")
                if a == "s":
                    self.chess.change_turn()
                    print("Es turno de: ", self.chess.__turn__)
                else:
                    print("Quieres guardar la partida? (y/n): ")
                    if input() == "y":
                        self.chess.save_game()
                        print("Partida guardada")
                          #poner esta parte del codigo con redis
            
            except (NotPieceToMove, NotPermitedMove, InvalidPosition, NotPieceToReplace) as e:
                print("Error:", e)
                print("Proba de nuevo", "sigue siendo el turno de ", self.chess.__turn__)

            except Exception as e:
                print("error", e)
                return "error"
            
        print("Fin del juego")


    #Valida que la posicion a la que te vas a mover este dentro del tablero
    def validate_range_to(self):
        while True:
            try:
                to_row = int(input("A fila: "))
                to_col = int(input("A colunma: "))
                self.chess.error_out_of_range(to_row, to_col)

                return to_row, to_col
            except ValueError:
                print("Invalid input. Please enter a number.")
            except InvalidPosition as e:
                print(e)


    #Verifica que el color de la pieza que queres mover sea tuyo
    def verify_color(self, chess, from_row, from_col):
        move_by_color = chess.move_correct_color(from_row, from_col)
        
        if move_by_color is None:
            return True  
        elif move_by_color == "No podes mover una pieza que no existe":
            print("No podes mover una pieza que no existe")
        else:
            print(move_by_color)
        
        return False


if __name__ == "__main__":
    cli = Cli()
    cli.play()