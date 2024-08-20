class Pieza:
    def __init__(self, equipo, posicion):
        self.equipo = equipo  # "blancas" o "negras"
        self.posicion = posicion  # Posición en el tablero, como (fila, columna)
        self.movimientos = []  # Movimientos posibles
        self.ataques = []  # Movimientos de ataque posibles

    def actualizar_movimientos(self):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas")

    def mover(self, nueva_posicion):
        if nueva_posicion in self.movimientos:
            self.posicion = nueva_posicion
            self.actualizar_movimientos()
            return True
        return False

    def atacar(self, objetivo_posicion):
        if objetivo_posicion in self.ataques:
            self.posicion = objetivo_posicion
            self.actualizar_movimientos()
            return True
        return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.equipo}, {self.posicion})"