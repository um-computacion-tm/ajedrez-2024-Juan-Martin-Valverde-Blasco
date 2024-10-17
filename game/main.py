from game.chess import Chess
from game.piece import Piece
from game.exceptions import InvalidPosition, NotPieceToMove, NotPermitedMove, NotPieceToReplace

class Cli():
 
    #Esta funcion lo que hace es uniciar todo el juego
    def __init__(self):
        self.chess = Chess()

    #Pide la posicion de la pieza que queres elegir, se fija que este dentro del tablero y si esta bien te imprime en la terminal la pieza que elejiste
    def verify_move(self, chess):
        while True:
            try:
                from_row = int(input("De fila: "))
                from_col = int(input("De columna: "))
                self.chess.error_out_of_range(from_row, from_col)
                print("La pieza que elejiste es: ", chess.__board__.piece_to_STR(from_row, from_col))
                if self.verify_color(chess, from_row, from_col):
                    return from_row, from_col
            except ValueError:
                print("Flasehaste, mete un numero")
            except InvalidPosition as e: #porque e? no se el gabi lo puso asi xd
                print(e)
                
                
    #Conjuncion de todas las funciones para poder jugar
    def client(self):
        self.welcome_message()
        self.main_menu1()
    
        game_running = True
    
        while game_running:
            a = input("Que queres hacer?: ")
            if a == "1":            
                while a == "1":
                    self.chess.__board__.show_board() 
                    try:
                        from_row, from_col = self.verify_move(self.chess)
                        to_row, to_col = self.validate_range()
    
                        print(self.chess.__board__.capture_piece(from_row, from_col, to_row, to_col))
                        self.chess.movement_fits(from_row, from_col, to_row, to_col) 
                        self.chess.change_pawn(from_row, from_col, to_row, to_col)
                        self.chess.__board__.show_board() 
                        print(self.chess.STR_captured_pieces())
    
                        if self.chess.verify_winner() is not False:
                            print(self.chess.verify_winner())
                            a = "3"
                            game_running = False
                            break
                        
                        self.main_menu2()
                        a = input("Que quieres hacer ahora?: ")
                        if a == "1":
                            self.chess.change_turn()
                            print("Es turno de: ", self.chess.__turn__)
                        elif a == "2":
                            self.show_tutorial()
                        elif a == "3":
                            break
                    except (NotPieceToMove, NotPermitedMove, InvalidPosition, NotPieceToReplace) as e:
                        print("Error:", e)
                        print("Try again", "It's still ", self.chess.__turn__, "turn")
                    except Exception as e:
                        print("Error", e)
                        return "Error"
    
                print("Game ended")
            elif a == "2":
                self.show_tutorial()
            elif a == "3":
                print("Game ended")
                game_running = False
            else:
                print("Invalid option")


    #Valida que la posicion a la que te vas a mover este dentro del tablero
    def validate_range(self):
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
        move_by_color = chess.right_color(from_row, from_col)
        
        if move_by_color is None:
            return True  
        elif move_by_color == "No podes mover una pieza que no existe":
            print("No podes mover una pieza que no existe")
        else:
            print(move_by_color)
        
        return False


    def welcome_message(self):
        print("--------------------------------------------------------------------------------------------")
        print("-------------------------Welcome to Ajedrez By Juan Martin Valverde-------------------------")
        print("----------------------------Tecnical consultor Copilot and GPT-4----------------------------")
        print("-------------------------Proyect For ComputacionI Ing informaticaUM-------------------------")
        print("--------------------------------------------------------------------------------------------")

    def main_menu1(self): 
        print("------------------------------------------Opciones---------------------------------------------")
        print("Presiona 1 para comenzar a jugar")
        print("Presiona 2 para ver un tutorial")
        print("Presiona 3 para salir")
        print("-----------------------------------------------------------------------------------------------")
        

    def main_menu2(self): 
        print("------------------------------------------Opciones---------------------------------------------")
        print("Presiona 1 para continuar jugando")
        print("Presiona 2 para ver un tutorial")
        print("Presiona 3 para salir")
        print("-----------------------------------------------------------------------------------------------")
        
                                                   
    def show_tutorial(self):
        self.tutorial_pawn_moves_and_attacks()
        self.tutorial_rook_moves_and_attacks()
        self.tutorial_knight_moves_and_attacks()
        self.tutorial_bishop_moves_and_attacks()
        self.tutorial_queen_moves_and_attacks()
        self.tutorial_king_moves_and_attacks()

            
    def tutorial_pawn_moves_and_attacks(self):
        print(
            "El movimiento y ataque del peón es el siguiente:\n"
            "El peón siempre se mueve un solo lugar hacia adelante.\n"
            "Si es el primer movimiento, puede avanzar dos lugares.\n"
            "El peón ataca en diagonal hacia adelante.\n"
            "    0     1     2\n"
            "  ═══════════════════\n"
            "4║     ║     ║     ║\n"
            "  ═══════════════════\n"
            "5║     ║  ♟  ║  X  ║\n"
            "  ═══════════════════\n"
            "6║  M  ║  ♟  ║     ║\n"
            "  ═══════════════════\n"
            "7║  ♟  ║     ║     ║\n"
            "  ═══════════════════\n"
            "  X marca las posibles casillas de ataque.\n"
            "  M marca las posibles casillas de movimiento."
            "\n-----------------------------------------\n")

        

    def tutorial_rook_moves_and_attacks(self):
        print(
            "El movimiento y ataque de la torre es el siguiente:\n"
            "La torre se mueve en línea recta, horizontal o vertical.\n"
            "No tiene limitación de distancia.\n"
            "    0     1     2     3     4\n"
            "  ═════════════════════════════\n"
            "0║  ♜  ║  X  ║  X  ║  X  ║  X  ║\n"
            "  ═════════════════════════════\n"
            "1║  X  ║     ║     ║     ║     ║\n"
            "  ═════════════════════════════\n"
            "2║  X  ║     ║     ║     ║     ║\n"
            "  ═════════════════════════════\n"
            "3║  X  ║     ║     ║     ║     ║\n"
            "  ═════════════════════════════\n"
            "4║  X  ║     ║     ║     ║     ║\n"
            "  ═════════════════════════════\n"
            "  X marca las posibles casillas de ataque y movimiento."
            "\n-----------------------------------------\n")


    def tutorial_knight_moves_and_attacks(self):
        print(
            "El movimiento y ataque del caballo es el siguiente:\n"
            "El caballo se mueve en forma de 'L': dos casillas en una dirección y luego una en ángulo recto.\n"
            "    0     1     2     3     4\n"
            "  ═════════════════════════════\n"
            "0║     ║     ║  X  ║     ║     ║\n"
            "  ═════════════════════════════\n"
            "1║     ║  X  ║     ║  X  ║     ║\n"
            "  ═════════════════════════════\n"
            "2║  X  ║     ║  ♞  ║     ║  X  ║\n"
            "  ═════════════════════════════\n"
            "3║     ║  X  ║     ║  X  ║     ║\n"
            "  ═════════════════════════════\n"
            "4║     ║     ║  X  ║     ║     ║\n"
            "  ═════════════════════════════\n"
            "  X marca las posibles casillas de ataque y movimiento."
            "\n-----------------------------------------\n")


    def tutorial_bishop_moves_and_attacks(self):
        print(
            "El movimiento y ataque del alfil es el siguiente:\n"
            "El alfil se mueve diagonalmente sin limitación de distancia.\n"
            "    0     1     2     3     4\n"
            "  ═════════════════════════════\n"
            "0║  X  ║     ║     ║     ║  X  ║\n"
            "  ═════════════════════════════\n"
            "1║     ║  X  ║     ║  X  ║     ║\n"
            "  ═════════════════════════════\n"
            "2║     ║     ║  ♝  ║     ║     ║\n"
            "  ═════════════════════════════\n"
            "3║     ║  X  ║     ║  X  ║     ║\n"
            "  ═════════════════════════════\n"
            "4║  X  ║     ║     ║     ║  X  ║\n"
            "  ═════════════════════════════\n"
            "  X marca las posibles casillas de ataque y movimiento."
            "\n-----------------------------------------\n")


    def tutorial_queen_moves_and_attacks(self):
        print(
            "El movimiento y ataque de la reina es el siguiente:\n"
            "La reina se mueve en todas las direcciones: horizontal, vertical y diagonal.\n"
            "    0     1     2     3     4\n"
            "  ═════════════════════════════\n"
            "0║  X  ║     ║  X  ║     ║  X  ║\n"
            "  ═════════════════════════════\n"
            "1║     ║  X  ║  X  ║  X  ║     ║\n"
            "  ═════════════════════════════\n"
            "2║  X  ║  X  ║  ♛  ║  X  ║  X  ║\n"
            "  ═════════════════════════════\n"
            "3║     ║  X  ║  X  ║  X  ║     ║\n"
            "  ═════════════════════════════\n"
            "4║  X  ║     ║  X  ║     ║  X  ║\n"
            "  ═════════════════════════════\n"
            "  X marca las posibles casillas de ataque y movimiento."
            "\n-----------------------------------------\n")


    def tutorial_king_moves_and_attacks(self):
        print(
            "El movimiento y ataque del rey es el siguiente:\n"
            "El rey se mueve una casilla en cualquier dirección: horizontal, vertical o diagonal.\n"
            "    0     1     2     3     4\n"
            "  ═════════════════════════════\n"
            "0║     ║     ║     ║     ║     ║\n"
            "  ═════════════════════════════\n"
            "1║     ║  X  ║  X  ║  X  ║     ║\n"
            "  ═════════════════════════════\n"
            "2║     ║  X  ║  ♚  ║  X  ║     ║\n"
            "  ═════════════════════════════\n"
            "3║     ║  X  ║  X  ║  X  ║     ║\n"
            "  ═════════════════════════════\n"
            "4║     ║     ║     ║     ║     ║\n"
            "  ═════════════════════════════\n"
            "  X marca las posibles casillas de ataque y movimiento."
            "\n-----------------------------------------\n"
            "\n---------------Mira Arriba---------------\n"
            "\n-----------------------------------------\n"
            )


            
if __name__ == "__main__":
    cli = Cli()
    cli.client()
    
#COMPLETE