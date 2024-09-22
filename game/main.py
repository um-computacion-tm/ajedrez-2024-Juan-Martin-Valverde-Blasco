from game.chess import Chess
from game.piece import Piece
from game.exceptions import InvalidPosition, NotPieceToMove, NotPermitedMove, NotPieceToReplace

class Cli():
    def main(self):
        self.play()

    def verify_move(self, chess): #Verifica el color del movimeinto

        while True:
            try:
                from_row = int(input("From row: "))
                from_col = int(input("From col: "))
                if not (0 <= from_row <= 7) or not (0 <= from_col <= 7):
                    raise InvalidPosition("Invalid position. Please enter a value between 0 and 7.")
                print("The piece you have chosen is: ", chess.__board__.get_piece(from_row, from_col))
                if self.verify_color(chess, from_row, from_col):
                    return from_row, from_col 
            except ValueError:
                print("Invalid input. Please enter a number.")
            except InvalidPosition as e:
                print(e)

    def play(self):
        chess = Chess()
        a = "s"
        try:
            while a.lower() == "s":
                from_row, from_col = self.verify_move(chess)

                to_row = int(input("A fil: "))
                to_col = int(input("A columna: "))

                chess.move(from_row, from_col, to_row, to_col)
                print("La pieza que quedo en la posicion es: ", chess.__board__.get_piece(from_row, from_col))
                print("La pieza que esta en la nueva posicion es: ", chess.__board__.get_piece(to_row, to_col))

                a = input("Queres seguir jugando? (s/n): ")

                if a.lower() == "s":
                    chess.change_turn()
                    print("Es turno de: ", chess.__turn__)

        except Exception as e:
            print("Error:", e)
            return "error"

    def validate_range_to(self):
        try:
            while True:
                to_row = int(input("To row: "))
                to_col = int(input("To col: "))
                if not (0 <= to_row <= 7) or not (0 <= to_col <= 7):
                    raise InvalidPosition("Invalid position. Please enter a value between 0 and 7.")
                break 

        except ValueError:
            print("Invalid input. Please enter a number.")
        except InvalidPosition as e:
            print(e)

        return to_row, to_col


if __name__ == "__main__":
    cli = Cli()
    cli.play()