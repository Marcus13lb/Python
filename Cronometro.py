import time

class Cronometro:
    @staticmethod
    def iniciar():
        return time.time()

    @staticmethod
    def detener():
        return time.time()

    @staticmethod
    def obtener_tiempo_transcurrido(inicio, fin=None):
        if fin is None:
            fin = time.time()
        return fin - inicio
