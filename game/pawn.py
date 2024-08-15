from game.piece import Pieza

class Peon(Pieza):
    def actualizar_movimientos(self):
        fila, columna = self.posicion
        self.movimientos = []
        self.ataques = []

        if self.equipo == "blancas":
            if fila > 0:
                self.movimientos.append((fila - 1, columna))
                if fila == 6:  # Movimiento doble desde la posición inicial
                    self.movimientos.append((fila - 2, columna))
        else:  # Peones negros
            if fila < 7:
                self.movimientos.append((fila + 1, columna))
                if fila == 1:  # Movimiento doble desde la posición inicial
                    self.movimientos.append((fila + 2, columna))

        if self.equipo == "blancas":
            if fila > 0 and columna > 0:
                self.ataques.append((fila - 1, columna - 1))
            if fila > 0 and columna < 7:
                self.ataques.append((fila - 1, columna + 1))
        else:  # Peones negros
            if fila < 7 and columna > 0:
                self.ataques.append((fila + 1, columna - 1))
            if fila < 7 and columna < 7:
                self.ataques.append((fila + 1, columna + 1))


# Ejemplo de uso
equipo_blanco = [Peon("blancas", (6, i)) for i in range(8)]
equipo_negro = [Peon("negras", (1, i)) for i in range(8)]

print(equipo_blanco)
print(equipo_negro)

peon_blanco = equipo_blanco[4]
print(f"Movimientos posibles para {peon_blanco}: {peon_blanco.movimientos}")
print(f"Ataques posibles para {peon_blanco}: {peon_blanco.ataques}")

peon_blanco.mover((4, 4))
print(f"Nueva posición del peón: {peon_blanco.posicion}")
print(f"Movimientos actualizados para {peon_blanco}: {peon_blanco.movimientos}")
print(f"Ataques actualizados para {peon_blanco}: {peon_blanco.ataques}")
