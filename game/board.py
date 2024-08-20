from game.rook import Rook
class Ajedrez:
    def __init__(self):
        self.tablero = self.inicializar_tablero()
        self.turno = "blancas"

    def inicializar_tablero(self):
        return [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]

    def imprimir_tablero(self):
        for fila in self.tablero:
            print(" ".join(fila))
        print()

    def convertir_coordenadas(self, coordenada):
        columnas = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
        filas = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
        columna = columnas[coordenada[0]]
        fila = filas[coordenada[1]]
        return (fila, columna)



if __name__ == "__main__":
    juego = Ajedrez()
    juego.jugar()
