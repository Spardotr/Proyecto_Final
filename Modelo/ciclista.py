from persona import Persona

class Ciclista(Persona):
    def __init__(self, identificador, contextura, nombre, cedula, especialidad=None):
        super().__init__(nombre, cedula)
        self.identificador = identificador
        self.contextura = contextura
        self.especialidad = especialidad
        self.tiempo = 0.0

    def get_identificador(self):
        return self.identificador

    def set_identificador(self, identificador):
        self.identificador = identificador

    def get_tiempo(self):
        return self.tiempo

    def set_tiempo(self, tiempo):
        self.tiempo = tiempo

    def get_especialidad(self):
        return self.especialidad

    def set_especialidad(self, especialidad):
        self.especialidad = especialidad

    def get_contextura(self):
        return self.contextura

    def set_contextura(self, contextura):
        self.contextura = contextura

    def imprimir_tipo(self):
        return f"Nombre: {self.nombre}\nIdentificador: {self.identificador}\nCedula: {self.cedula}\nContextura: {self.contextura}"
