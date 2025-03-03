from ciclista import Ciclista
from muestra import Muestra

class Escalador(Ciclista, Muestra):
    def __init__(self, aceleracion_subida, grado_rampa, identificador, contextura, nombre, cedula, especialidad=None):
        super().__init__(identificador, contextura, nombre, cedula, especialidad)
        self.aceleracion_subida = aceleracion_subida
        self.grado_rampa = grado_rampa

    def muestra_datos(self):
        return f"Nombre: {self.nombre}\nAceleración de subida: {self.aceleracion_subida}\nGrado de Rampa: {self.grado_rampa}"

    def imprimir_tipo(self):
        return super().imprimir_tipo() + " Es un Escalador"
