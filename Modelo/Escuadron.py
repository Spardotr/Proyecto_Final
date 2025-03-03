class Escuadron:
    def __init__(self, nombre_escuadron, pais=None, masajista=None):
        self.nombre_escuadron = nombre_escuadron
        self.pais = pais
        self.masajista = masajista
        self.ciclistas = []
        self.tiempo_ciclistas = 0.0

    def set_ciclistas(self, ciclistas):
        self.ciclistas = ciclistas

    def sumar_tiempos(self, tiempo):
        self.tiempo_ciclistas += tiempo

    def dar_arreglo(self, indice):
        return self.ciclistas[indice]
