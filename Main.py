import tkinter as tk
from Tablero import Tablero
from vista.VistaBuscaminas import VistaBuscaminas
from controlador.ControladorBuscaminas import ControladorBuscaminas

def main():
    root = tk.Tk()
    filas = 12
    columnas = 16
    num_minas = 15

    model = Tablero(filas, columnas, num_minas)
    model.coloca_minas()

    # Crear controlador y vista
    view = VistaBuscaminas(root, model, controller=None) 
    controller = ControladorBuscaminas(view, model)

    root.mainloop()

if __name__ == "__main__":
    main()
