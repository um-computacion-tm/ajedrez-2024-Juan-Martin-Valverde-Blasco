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
        a = "y"
        
        while a == "y":
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

    def verify_color(self, chess, from_row, from_col):
        move_by_color = chess.move_correct_color(from_row, from_col)
        
        if move_by_color is None:
            return True  
        elif move_by_color == "You can't move a piece that doesn't exist":
            print("You can't move a piece that doesn't exist")
        else:
            print(move_by_color)
        
        return False


if __name__ == "__main__":
    cli = Cli()
    cli.play()