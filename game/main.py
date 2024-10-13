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
                self.chess.change_pawn(from_row, from_col, to_row, to_col)
                self.chess.__board__.show_board() 
                print(self.chess.STR_captured_pieces())
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
        move_by_color = chess.right_color(from_row, from_col)
        
        if move_by_color is None:
            return True  
        elif move_by_color == "No podes mover una pieza que no existe":
            print("No podes mover una pieza que no existe")
        else:
            print(move_by_color)
        
        return False



#    def show_game_options(self):
#        print("-------------------------------------Tablero del Ajedrez---------------------------------------")
#        self.chess.__board__.show_board() 
#        print("------------------------------------------Opciones---------------------------------------------")
#        print("Presiona 1 para seguir jugando o tirar la espada al mar")
#        print("Presiona 2 para cambiar un peon")
#        print("Presiona 3 para guardar partida")
#        print("-----------------------------------------------------------------------------------------------")
#        print("Es el turno de ",self.chess.__turn__)
#    
#
#
#    def handle_user_input(self, option):
#        
#        if option == 1:
#            try:
#                from_row, from_col = self.verify_move(self.chess)
#                to_row, to_col = self.validate_range_to()
#                print(self.chess.__board__.capture_piece(from_row, from_col, to_row, to_col))
#                self.chess.movement_fits(from_row, from_col,to_row,to_col) 
#                self.chess.change_pawn(from_row, from_col, to_row, to_col)
#                self.chess.__board__.show_board() 
#                print(self.chess.STR_captured_pieces())
#                if self.chess.verify_winner() is not False:
#                    print(self.chess.verify_winner())
#                self.chess.change_turn()
#                    
#            except (NotPieceToMove, NotPermitedMove, InvalidPosition, NotPieceToReplace) as e:
#                print("Error:", e)
#                print("Proba de nuevo", "sigue siendo el turno de ", self.chess.__turn__)
#
#            except Exception as e:
#                print("error", e)
#                return "error"
#
#            print("Fin del juego")
#        elif option == 2:
#          self.handle_option_2()
#        elif option == 3:
#          self.handle_option_3()
#        elif option == 4:
#            self.handle_option_4()
#        else:
#            print("Incorrect Input. Please try again.")
#            self.show_game_options()
#            
#    def handle_option_2(self):
#        tiles_to_exchange_indices = input("Enter the indices of tiles you want to exchange (comma-separated): ").split(',')
#        old_tiles_indices = [int(index.strip()) for index in tiles_to_exchange_indices]
#        exchanged_tiles = self.scrabble.exchange_tiles(old_tiles_indices)
#        print("Exchanged tiles: ", exchanged_tiles)
#        self.scrabble.next_turn()
#
#    def handle_option_3(self):
#        print('Okay, exchanging all your tiles')
#        exchanged_tiles = self.scrabble.exchange_all_tiles()
#        print("Exchanged tiles: ", exchanged_tiles)
#        self.scrabble.next_turn()
#
#    def handle_option_4(self):
#        print("Well, passing to the next player...")
#        self.scrabble.next_turn()
#
#
#    def client(self):
#        self.welcome_message()
#        player_count = self.get_player_count()
#        self.scrabble = ScrabbleGame(total_players=player_count)
#
#        while self.scrabble.is_playing():
#            self.scrabble.next_turn()
#            self.scrabble.start_game()
#
#            while True:
#                self.show_game_options()
#                try:
#                    option = int(input("Choose your Option: "))
#                    self.handle_user_input(option)
#                except ValueError:
#                    print("Invalid input. Please enter a valid number.")
#                except Exception as e:
#                    print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    cli = Cli()
    cli.play()