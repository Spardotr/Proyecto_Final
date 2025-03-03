from ciclista import Ciclista
from muestra import Muestra

class Clasicomano(Ciclista, Muestra):
    def __init__(self, clasicos_ganados, identificador, contextura, nombre, cedula, especialidad=None):
        super().__init__(identificador, contextura, nombre, cedula, especialidad)
        self.clasicos_ganados = clasicos_ganados

    def get_clasicos_ganados(self):
        return self.clasicos_ganados

    def set_clasicos_ganados(self, clasicos_ganados):
        self.clasicos_ganados = clasicos_ganados

    def muestra_datos(self):
        return f"Nombre: {self.nombre}\nClasicos Ganados: {self.clasicos_ganados}"

    def imprimir_tipo(self):
        return super().imprimir_tipo() + " Es un Clasicomano"
