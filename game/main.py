from game.chess import Chess
from game.piece import Piece

from game.exceptions import InvalidPosition, NotPieceToMove, NotPermitedMove, NotPieceToReplace, GameEnded

class Cli():
    def __init__(self):
        self.chess = Chess()

    def main(self):
        self.play()

    def verify_move(self, chess): #Verifica el color del movimeinto

        while True:
            try:
                from_row = int(input("From row: "))
                from_col = int(input("From col: "))
              
                self.chess.verify_out_of_range(from_row, from_col)

                print("The piece you have chosen is: ", chess.__board__.get_piece_for_show(from_row, from_col))
            
                # Verificamos el color de la pieza usando la nueva función
                if self.verify_color(chess, from_row, from_col):
                    return from_row, from_col  # Si la verificación es exitosa, retornamos las coordenadas
    

            except ValueError:
                print("Invalid input. Please enter a number.")
            except InvalidPosition as e:
                print(e)

    def verify_color(self, chess, from_row, from_col):
        move_by_color = chess.move_correct_color(from_row, from_col)
        
        if move_by_color is None:  # Si no hay error, se seleccionó la pieza correcta
            return True  # Verificación exitosa
        elif move_by_color == "You can't move a piece that doesn't exist":
            print("You can't move a piece that doesn't exist")
        else:
            print(move_by_color)
        
        return False  # Verificación fallida


    def play(self):
        # chess = Chess()
        #board = Board() #No se usa porque si creo un board aca esoy inhiendo al otro board, estoy como creando un board nuevo que no le he movido ninguna pieza
        a = "y"
        
        while a == "y":
            self.chess.__board__.show_board() 
            try:
                from_row, from_col = self.verify_move(self.chess)

                to_row, to_col = self.validate_range_to()

                print(self.chess.__board__.eat_piece(from_row, from_col, to_row, to_col))
                # Quiero hacer que si move levanta excepcion, vuelva a ejecutar play -- LISTO
                self.chess.move(from_row, from_col,to_row,to_col) 

                self.chess.change_pawn_for_other(from_row, from_col, to_row, to_col)

                self.chess.__board__.show_board() 
            
                print(self.chess.show_eaten_pieces())

                if self.chess.verify_winner() is not False:
                    print(self.chess.verify_winner())
                    a = "n"
                    break
                a = input("Do you want to continue? (y/n): ")
                if a == "y":
                    self.chess.change_turn()
                    print("Es turno de: ", self.chess.__turn__)

            except (NotPieceToMove, NotPermitedMove, InvalidPosition, NotPieceToReplace) as e:
                print("Error:", e)
                print("Try again", "It's still ", self.chess.__turn__, "turn")

            except Exception as e:
                print("error", e)
                return "error"
            
        print("Game ended")


    def validate_range_to(self):
        while True:
            try:
                to_row = int(input("To row: "))
                to_col = int(input("To col: "))

                self.chess.verify_out_of_range(to_row, to_col)

                return to_row, to_col

            except ValueError:
                print("Invalid input. Please enter a number.")
            except InvalidPosition as e:
                print(e)



if __name__ == "__main__":
    cli = Cli()
    cli.play()