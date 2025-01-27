# Proyecto_Final


```mermaid
  classDiagram
    class Persona {
        - nombre: String
        - cedula: int
    }

    class Ciclista {
        - identificador: int
        - tiempo: double
        - especialidad: String
        - contextura: String
        + getIdentificador(): int
        + setIdentificador(identificador: int)
        + getTiempo(): double
        + setTiempo(tiempo: double)
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
        - velocidad_maxima: double
        + getVelocidad_maxima(): double
        + setVelocidad_maxima(velocidad_maxima: double)
    }

    class Embalador {
        - potencia_promedio: double
        - velocidad_promedio: double
        + getPotencia_promedio(): double
        + setPotencia_promedio(potencia_promedio: double)
        + getVelocidad_promedio(): double
        + setVelocidad_promedio(velocidad_promedio: double)
    }

    class Escalador {
        - aceleracion_subida: double
        - grado_rampa: double
        + getAceleracion_subida(): double
        + setAceleracion_subida(aceleracion_subida: double)
        + getGrado_rampa(): double
        + setGrado_rampa(grado_rampa: double)
    }

    class Rodador {
        - pedaleo: double
        + getPedaleo(): double
        + setPedaleo(pedaleo: double)
    }

    class Gregario {
        - funcion_peloton: String
        + getFuncion_peloton(): String
        + setFuncion_peloton(funcion_peloton: String)
    }

    class Escuadron {
        - nombre_escuadron: String
        - pais: String
        - tiempo_ciclistas: double
        - ciclistas: Ciclista[]
        - masajista: Masajista
        + sumarTiempos(tiempo: double)
    }

    class Masajista {
        + getCedula(): int
        + setCedula(cedula: int)
    }

    class Funcion_peloton {
        <<enumeration>>
        ABASTECEDOR
        MANTENER_EL_RITMO
        CAPTURA_DE_FUGAS
        POSICIONAR_AL_LIDER
        PROTEGER_AL_LIDER
    }

    class Muestra {
        <<interface>>
        + muestraDatos(): String
    }

    class MuestraCadencia {
        <<interface>>
        + muestraCadencia(): String
    }

    class Preparable {
        <<interface>>
        + prepararse(): String
    }

    class Preparable_contrarrelojista {
        <<interface>>
        + visualizar(): String
        + concentrarse(): String
    }

    class Preparable_embalador {
        <<interface>>
        + aumentar_ritmo(): String
        + bajar_ritmo(): String
    }

    class Preparable_escalador {
        <<interface>>
        + pedalear_sentado(): String
        + pedalear_depie(): String
    }

    Persona <|-- Ciclista
    Ciclista <|-- Clasicomano
    Ciclista <|-- Contrarrelojista
    Ciclista <|-- Embalador
    Ciclista <|-- Escalador
    Ciclista <|-- Rodador
    Ciclista <|-- Gregario
    Escuadron --> Ciclista : tiene
    Escuadron --> Masajista : incluye
    Gregario --> Funcion_peloton : usa
    Rodador ..|> MuestraCadencia
    Rodador ..|> Muestra
    Gregario ..|> Muestra
    Escalador ..|> Preparable_escalador
    Embalador ..|> Preparable_embalador
    Contrarrelojista ..|> Preparable_contrarrelojista
    Ciclista ..|> Preparable
