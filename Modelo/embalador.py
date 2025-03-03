from ciclista import Ciclista
from muestra import Muestra

class Embalador(Ciclista, Muestra):
    def __init__(self, potencia_promedio, velocidad_promedio, identificador, contextura, nombre, cedula, especialidad=None):
        super().__init__(identificador, contextura, nombre, cedula, especialidad)
        self.potencia_promedio = potencia_promedio
        self.velocidad_promedio = velocidad_promedio

    def muestra_datos(self):
        return f"Nombre: {self.nombre}\nPotencia Promedio: {self.potencia_promedio}\nVelocidad Promedio: {self.velocidad_promedio}"

    def imprimir_tipo(self):
        return super().imprimir_tipo() + " Es un Embalador"
