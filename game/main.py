from game.chess import Chess
from game.piece import Piece
from game.exceptions import InvalidPosition, NotPieceToMove, NotPermitedMove, NotPieceToReplace

class Cli():
    def __init__(self):
        self.chess = Chess()

    def main(self):
        self.play()

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
                
                
    def play(self):
        a = "s"        
        while a == "s":
            self.chess.__board__.show_board() 
            try:
                from_row, from_col = self.verify_move(self.chess)

                to_row, to_col = self.validate_range_to()

                print(self.chess.__board__.eat_piece(from_row, from_col, to_row, to_col))
                self.chess.movement_fits(from_row, from_col,to_row,to_col) 

                self.chess.change_pawn_for_other(from_row, from_col, to_row, to_col)

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

            except (NotPieceToMove, NotPermitedMove, InvalidPosition, NotPieceToReplace) as e:
                print("Error:", e)
                print("Proba de nuevo", "sigue siendo el turno de ", self.chess.__turn__)

            except Exception as e:
                print("error", e)
                return "error"
            
        print("Fin del juego")


    def validate_range_to(self):
        try:
            while True:
                to_row = int(input("A fila: "))
                to_col = int(input("A columna: "))
                if not (0 <= to_row <= 7) or not (0 <= to_col <= 7):
                    raise InvalidPosition("Posicion invalida, debe estar entre 0 y 7.")
                break 

        except ValueError:
            print("Flasheaste, mete un numero")
        except InvalidPosition as e:
            print(e)

        return to_row, to_col

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