import random
import time


from escuadron import Escuadron
from ciclista import Ciclista
from clasicomano import Clasicomano
from contrarrelojista import Contrarrelojista
from embalador import Embalador
from escalador import Escalador
from gregario import Gregario
from fisioterapeuta import Fisioterapeuta
from rodador import Rodador
from vista import Vista


class Gestor:
    def __init__(self):
        self.vista = Vista()
        self.contador = 0
        self.contador_escuadrones = 1
        self.ciclistas = [None] * 6
        self.escuadron1 = None
        self.escuadron2 = None
        self.escuadron3 = None

    def crear_escuadron(self, nombre_escuadron, pais=None, masajista=None):
        escuadron = Escuadron(nombre_escuadron, pais, masajista)
        return escuadron

    def iniciar_carrera(self, tipo_etapa):
        for escuadron in [self.escuadron1, self.escuadron2, self.escuadron3]:
            self.calcular_tiempos(escuadron, tipo_etapa)

        print("Iniciando carrera...")

        progreso = 0
        while progreso < 100:
            time.sleep(1)  # Simulación de progreso
            progreso += 20
            print(f"Progreso de la carrera: {progreso}%")

        self.declarar_ganador()

    def calcular_tiempos(self, escuadron, especialidad):
        tiempo_total = 0
        for ciclista in escuadron.ciclistas:
            if ciclista.get_especialidad() == especialidad:
                tiempo = random.randint(18000, 36000)
                ciclista.set_tiempo(tiempo)
                tiempo_total += tiempo

        escuadron.sumar_tiempos(tiempo_total)

    def declarar_ganador(self):
        tiempos = {
            self.escuadron1: self.escuadron1.tiempo_ciclistas,
            self.escuadron2: self.escuadron2.tiempo_ciclistas,
            self.escuadron3: self.escuadron3.tiempo_ciclistas
        }

        ganador = min(tiempos, key=tiempos.get)
        print(f"El ganador de la carrera es el escuadrón {ganador.nombre_escuadron}")

