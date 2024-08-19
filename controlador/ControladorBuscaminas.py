import tkinter as tk

class ControladorBuscaminas:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        # Configura la vista inicial
        self.view.mostrar_tablero()

        # Maneja clics en las casillas
        for i in range(self.model.filas):
            for j in range(self.model.columnas):
                self.view.botones[i * self.model.columnas + j].config(command=lambda y=i, x=j: self.clic_casilla(y, x))

    def clic_casilla(self, y, x):
        tablero_visible = self.model.get_tablero_visible()
        tablero_oculto = self.model.get_tablero_oculto()

        if tablero_oculto[y][x] == 9:
            tablero_visible[y][x] = "@"
            self.view.mostrar_tablero()
            tiempo_transcurrido = self.view.detener_cronometro()
            self.view.mostrar_mensaje(f"¡Has perdido! Tiempo: {tiempo_transcurrido:.1f} segundos")
            self.view.deshabilitar_botones()
        elif tablero_oculto[y][x] != 0:
            tablero_visible[y][x] = tablero_oculto[y][x]
        else:
            tablero_visible[y][x] = 0
            self.model.descubre_ceros(y, x)

        self.view.mostrar_tablero()

        if self.model.tablero_completo():
            tiempo_transcurrido = self.view.detener_cronometro()
            self.view.mostrar_mensaje(f"¡Has ganado! Tiempo: {tiempo_transcurrido:.1f} segundos")
            self.view.deshabilitar_botones()
