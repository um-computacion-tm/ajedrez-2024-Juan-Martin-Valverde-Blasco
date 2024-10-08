from game.chess import Chess
from game.board import Board

class Cli():
    def main(self):
        self.play()

    def verify_move(self, chess):
        while True:
            from_row = int(input("De fila: "))
            from_col = int(input("De columna: "))
            print("La pieza que elegiste es: ", chess.__board__.get_piece(from_row, from_col))
            
            move_by_color = chess.move_correct_color(from_row, from_col)
            if move_by_color is None:  
                return from_row, from_col
            else:
                print(move_by_color)  

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

if __name__ == "__main__":
    cli = Cli()
    cli.play()