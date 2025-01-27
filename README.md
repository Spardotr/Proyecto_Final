# Proyecto_Final


```mermaid
  classDiagram
    class Persona {
        - nombre: String
        - cedula: int
    }

    class Ciclista {
        - identificador: int
        - tiempo: float
        - especialidad: String
        - contextura: String
        + getIdentificador(): int
        + setIdentificador(identificador: int)
        + getTiempo(): float
        + setTiempo(tiempo: float)
        + getEspecialidad(): String
        + setEspecialidad(especialidad: String)
        + getContextura(): String
        + setContextura(contextura: String)
    }

    class Clasicomano {
        - clasicos_ganados: int
        + getClasicos_ganados(): int
        + setClasicos_ganados(clasicos_ganados: int)
    }

    class Contrarrelojista {
        - velocidad_maxima: float
        + visualizar(): String
        + concentrarse(): String
        + getVelocidad_maxima(): float
        + setVelocidad_maxima(velocidad_maxima: float)
    }

    class Embalador {
        - potencia_promedio: float
        - velocidad_promedio: float
        + aumentar_ritmo(): String
        + bajar_ritmo(): String
        + getPotencia_promedio(): float
        + setPotencia_promedio(potencia_promedio: float)
        + getVelocidad_promedio(): float
        + setVelocidad_promedio(velocidad_promedio: float)
    }

    class Escalador {
        - aceleracion_subida: float
        - grado_rampa: float
        + pedalear_sentado(): String
        + pedalear_depie(): String
        + getAceleracion_subida(): float
        + setAceleracion_subida(aceleracion_subida: float)
        + getGrado_rampa(): float
        + setGrado_rampa(grado_rampa: float)
    }

    class Rodador {
        - pedaleo: float
        + getPedaleo(): float
        + setPedaleo(pedaleo: float)
    }

    class Gregario {
        - funcion_peloton: String
        + getFuncion_peloton(): String
        + setFuncion_peloton(funcion_peloton: String)
    }

    class Escuadron {
        - nombre_escuadron: String
        - pais: String
        - tiempo_ciclistas: float
        - ciclistas: Ciclista[]
        - fisioterapeuta : Fisioterapeuta
        + sumarTiempos(tiempo: float)
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
    Escuadron --> Ciclista 
    Escuadron --> Fisioterapeuta 
    Gregario --> Funcion_peloton 

