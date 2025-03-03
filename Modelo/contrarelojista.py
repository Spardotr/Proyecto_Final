from ciclista import Ciclista
from muestra import Muestra

class Contrarrelojista(Ciclista, Muestra):
    def __init__(self, velocidad_maxima, identificador, contextura, nombre, cedula, especialidad=None):
        super().__init__(identificador, contextura, nombre, cedula, especialidad)
        self.velocidad_maxima = velocidad_maxima

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def muestra_datos(self):
        return f"Nombre: {self.nombre}\nVelocidad Máxima: {self.velocidad_maxima}"

    def imprimir_tipo(self):
        return super().imprimir_tipo() + " Es un Contrarrelojista"
