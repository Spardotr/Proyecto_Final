from ciclista import Ciclista
from muestra_cadencia import MuestraCadencia
from muestra import Muestra

class Rodador(Ciclista, MuestraCadencia, Muestra):
    def __init__(self, pedaleo: float, identificador: int, contextura: str, nombre: str, cedula: int, especialidad=None):
        super().__init__(identificador, contextura, nombre, cedula, especialidad)
        self.pedaleo = pedaleo

    def get_pedaleo(self):
        return self.pedaleo

    def set_pedaleo(self, pedaleo):
        self.pedaleo = pedaleo

    def muestra_datos(self):
        return f"Nombre: {self.nombre}\n"

    def muestra_cadencia(self):
        return f"Cadencia de Pedaleo: {self.pedaleo}"

    def imprimir_tipo(self):
        return super().imprimir_tipo() + " Es un Rodador"
