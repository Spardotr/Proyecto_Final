# Proyecto_Final
Definicion del Problema

El proyecto esta hecho para simular la dinamica de una carrera profesional de equipos de ciclistas (Escuadrones). Este sistema gestiona y modela los roles de cada ciclista, las condiciones de cada carrera, y las estadisticas de los resultados. Los elementos principales a explicar son los siguientes:

1. Escuadrón

Cada escuadrón debe cumplir con los siguientes requisitos:


Contar con exactamente 6 ciclistas, distribuidos en roles específicos:


-Escalador: Especialista en etapas de montaña, con habilidades como aceleración en subida y manejo de pendientes.

-Rodador: Destacado en etapas llanas por su pedaleo constante y alta cadencia.

-Embalador: Enfocado en sprints finales, con alta velocidad y potencia promedio.

-Gregario: Ciclista de apoyo, que protege al líder y mantiene el ritmo del equipo.

-Clasicómano: Experto en carreras de un día o clásicas, con equilibrio entre velocidad y resistencia.

-Contrarrelojista: Ciclista con alta velocidad máxima, ideal para etapas individuales.


El escuadrón tiene:


-Un nombre.

-Un país de origen (opcional).

-Un atributo estático que registra el tiempo acumulado de todos sus ciclistas.


2. Ciclistas


Cada ciclista cuenta con:


-Identificador único, nombre, y tiempo acumulado (inicia en 0 minutos).

-Especialidad y contextura, que afectan su desempeño en las carreras.

-Resistencia y energía, atributos dinámicos que cambian según las condiciones de las carreras.


3. Simulación de carreras


Los escuadrones participan en diferentes tipos de carreras:


-Etapas de montaña, llanos con curvas, semi llanos, carreras de un solo día, y llanos en recta.

Según el tipo de carrera, se selecciona al ciclista más adecuado para competir.

Los gregarios no compiten directamente, pero apoyan al líder del escuadrón.


Durante la carrera:


-A cada ciclista se le asigna un tiempo aleatorio no mayor a 36,000 segundos.

-Factores como clima (lluvioso, soleado) y dificultad de la etapa afectan el rendimiento.

-Eventos aleatorios, como fallos mecánicos o caídas, penalizan o benefician el tiempo de los ciclistas.


5. Resultados y estadísticas


Al finalizar la carrera, se generan los siguientes datos:


-Tiempos acumulados por escuadrón.

-Ciclistas destacados.

-Ganador de la etapa, con información detallada del ciclista y su escuadrón.

```mermaid
  classDiagram
    class Persona {
        - nombre: String
        - cedula: int
    }

    class Ciclista {
        - identificador: int
        - tiempo: Float
        - especialidad: String
        - contextura: String
        - resistencia: int
        - energia: int
        + calcularDesempeno(tipoEtapa: String, clima: String): Float
        + getIdentificador(): int
        + setIdentificador(identificador: int)
        + getTiempo(): Float
        + setTiempo(tiempo: Float)
        + getEspecialidad(): String
        + setEspecialidad(especialidad: String)
        + getContextura(): String
        + setContextura(contextura: String)
        + getResistencia(): int
        + setResistencia(resistencia: int)
        + getEnergia(): int
        + setEnergia(energia: int)
    }

    class Clasicomano {
        - clasicos_ganados: int
        + getClasicos_ganados(): int
        + setClasicos_ganados(clasicos_ganados: int)
    }

    class Contrarrelojista {
        - velocidad_maxima: Float
        + visualizar(): String
        + concentrarse(): String
        + getVelocidad_maxima(): Float
        + setVelocidad_maxima(velocidad_maxima: Float)
    }

    class Embalador {
        - potencia_promedio: Float
        - velocidad_promedio: Float
        + aumentar_ritmo(): String
        + bajar_ritmo(): String
        + getPotencia_promedio(): Float
        + setPotencia_promedio(potencia_promedio: Float)
        + getVelocidad_promedio(): Float
        + setVelocidad_promedio(velocidad_promedio: Float)
    }

    class Escalador {
        - aceleracion_subida: Float
        - grado_rampa: Float
        + pedalear_sentado(): String
        + pedalear_depie(): String
        + getAceleracion_subida(): Float
        + setAceleracion_subida(aceleracion_subida: Float)
        + getGrado_rampa(): Float
        + setGrado_rampa(grado_rampa: Float)
    }

    class Rodador {
        - pedaleo: Float
        + getPedaleo(): Float
        + setPedaleo(pedaleo: Float)
    }

    class Gregario {
        - funcion_peloton: String
        + getFuncion_peloton(): String
        + setFuncion_peloton(funcion_peloton: String)
    }

    class Escuadron {
        - nombre_escuadron: String
        - pais: String
        - tiempo_ciclistas: Float
        - ciclistas: Ciclista[]
        - fisioterapeuta : Fisioterapeuta
        - estrategia: String
        + seleccionarLider(): Ciclista
        + apoyarLider(lider: Ciclista)
        + generarEventosAleatorios(ciclista: Ciclista)
        + calcularEstadisticas(): String
    }

    class Entrenador {
        + entrenar(Ciclista ciclista)
    }

    class Carrera {
        - tipoEtapa: String
        - clima: String
        - dificultad: int
        + simular(Escuadron[] escuadrones)
        + afectarAtributos(Ciclista ciclista)
    }

    class Fisioterapeuta {
        + getCedula(): int
        + setCedula(cedula: int)
    }



    Persona <|-- Ciclista
    Ciclista <|-- Clasicomano
    Ciclista <|-- Contrarrelojista
    Ciclista <|-- Embalador
    Ciclista <|-- Escalador
    Ciclista <|-- Rodador
    Ciclista <|-- Gregario
    Escuadron --> Ciclista : tiene
    Escuadron --> Fisioterapeuta : incluye un
    Escuadron --> Entrenador : tiene un
    Escuadron --> Carrera : participa
