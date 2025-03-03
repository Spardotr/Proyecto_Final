from ciclista import Ciclista
from muestra import Muestra

class Gregario(Ciclista, Muestra):
    def __init__(self, funcion_peloton, identificador, contextura, nombre, cedula, especialidad=None):
        super().__init__(identificador, contextura, nombre, cedula, especialidad)
        self.funcion_peloton = funcion_peloton

    def muestra_datos(self):
        return f"Nombre: {self.nombre}\nFunción en el Pelotón: {self.funcion_peloton}"

    def imprimir_tipo(self):
        return super().imprimir_tipo() + " Es un Gregario"
