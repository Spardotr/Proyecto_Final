# Proyecto_Final


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
        + entrenar(Ciclista ciclista): void
    }

    class Carrera {
        - tipoEtapa: String
        - clima: String
        - dificultad: int
        + simular(Escuadron[] escuadrones): void
        + afectarAtributos(Ciclista ciclista): void
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
