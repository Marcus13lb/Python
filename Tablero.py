import random

#Modelo del juego Buscaminas.

class Tablero:
    def __init__(self, filas, columnas, num_minas):
        self.filas = filas
        self.columnas = columnas
        self.num_minas = num_minas
        self.tablero_oculto = self.crea_tablero(filas, columnas, 0)
        self.tablero_visible = self.crea_tablero(filas, columnas, "-")
        self.minas_ocultas = []

    def crea_tablero(self, fil, col, val):
        return [[val for _ in range(col)] for _ in range(fil)]

    def coloca_minas(self):
        numero = 0
        while numero < self.num_minas:
            y = random.randint(0, self.filas - 1)
            x = random.randint(0, self.columnas - 1)
            if self.tablero_oculto[y][x] != 9:
                self.tablero_oculto[y][x] = 9
                numero += 1
                self.minas_ocultas.append((y, x))

        self.coloca_pistas()

    def coloca_pistas(self):
        for y in range(self.filas):
            for x in range(self.columnas):
                if self.tablero_oculto[y][x] == 9:
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if 0 <= y + i < self.filas and 0 <= x + j < self.columnas:
                                if self.tablero_oculto[y + i][x + j] != 9:
                                    self.tablero_oculto[y + i][x + j] += 1

    def descubre_ceros(self, y, x):
        ceros = [(y, x)]
        while ceros:
            y, x = ceros.pop()
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if 0 <= y + i < self.filas and 0 <= x + j < self.columnas:
                        if self.tablero_visible[y + i][x + j] == "-" and self.tablero_oculto[y + i][x + j] == 0:
                            self.tablero_visible[y + i][x + j] = 0
                            ceros.append((y + i, x + j))
                        else:
                            self.tablero_visible[y + i][x + j] = self.tablero_oculto[y + i][x + j]

    def get_tablero_visible(self):
        return self.tablero_visible

    def get_tablero_oculto(self):
        return self.tablero_oculto

    def get_minas_ocultas(self):
        return self.minas_ocultas

    def tablero_completo(self):
        for y in range(self.filas):
            for x in range(self.columnas):
                if self.tablero_visible[y][x] == "-" and self.tablero_oculto[y][x] != 9:
                    return False
        return True
