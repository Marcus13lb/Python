import tkinter as tk
from Cronometro import Cronometro

class VistaBuscaminas:
    def __init__(self, root, model, controller):
        self.root = root
        self.model = model
        self.controller = controller 
        self.botones = []
        self.cronometro = Cronometro
        self.tiempo_inicio = self.cronometro.iniciar()
        self.label_tiempo = tk.Label(self.root, text="Tiempo: 0s")
        self.label_tiempo.grid(row=self.model.filas, columnspan=self.model.columnas)

        self.crear_interfaz()

    def crear_interfaz(self):
        self.root.title("Buscaminas")

        for i in range(self.model.filas):
            for j in range(self.model.columnas):
                boton = tk.Button(self.root, width=2, height=1,
                                  command=lambda y=i, x=j: self.click_casilla(y, x))
                boton.grid(row=i, column=j)
                self.botones.append(boton)


        # Actualizar el tiempo cada segundo
        self.actualizar_cronometro()

    def mostrar_tablero(self):
        tablero_visible = self.model.get_tablero_visible()
        for i in range(self.model.filas):
            for j in range(self.model.columnas):
                valor = tablero_visible[i][j]
                self.botones[i * self.model.columnas + j].config(text=str(valor))

    def actualizar_cronometro(self):
        tiempo_transcurrido = int(self.cronometro.obtener_tiempo_transcurrido(self.tiempo_inicio))
        self.label_tiempo.config(text=f"Tiempo: {tiempo_transcurrido}s")
        self.root.after(1000, self.actualizar_cronometro)  # Llamar de nuevo después de 1 segundo

    def detener_cronometro(self):
        tiempo_fin = self.cronometro.detener()
        tiempo_transcurrido = self.cronometro.obtener_tiempo_transcurrido(self.tiempo_inicio, tiempo_fin)
        return tiempo_transcurrido

    # Métodos para manejar eventos de juego (como clics en casillas, mensajes de victoria/derrota, etc.)
    def clic_casilla(self, y, x):
        self.controller.clic_casilla(y, x)

    def mostrar_mensaje(self, mensaje):
        label_mensaje = tk.Label(self.root, text=mensaje)
        label_mensaje.grid(row=self.model.filas + 1, columnspan=self.model.columnas)
        self.root.update()  # Actualizar la ventana

    def deshabilitar_botones(self):
        # Deshabilitar todos los botones para evitar más clics
        for boton in self.botones:
            boton.config(state=tk.DISABLED)
