# 🚴‍♂️ Simulación de Carrera de Ciclistas

**📌 Descripción:**  
Este proyecto simula una carrera de ciclistas utilizando una interfaz gráfica y una ejecución en consola. Se modelan escuadrones de ciclistas con distintos roles y se ejecutan carreras en diversas etapas.

---

## 🎯 **Planteamiento del Problema**
El problema consiste en simular una competencia entre ciclistas, donde cada escuadrón contiene 6 ciclistas con roles distintos:  
- **Escalador**
- **Rodador**
- **Embalador**
- **Gregario**
- **Clasicómano**
- **Contrarrelojista**

Cada ciclista tiene atributos como **nombre, identificador, especialidad, cédula y tiempo de carrera acumulado**.  
Los escuadrones pueden competir en distintas **etapas de carrera** con condiciones específicas.

---

## 💡 **Solución Implementada**
- Se modeló cada ciclista como una clase en Python con **POO (Programación Orientada a Objetos)**.
- Se creó una clase `Escuadron` que contiene a los ciclistas y gestiona su información.
- Se implementó un **`Gestor`** que maneja la lógica de la carrera.
- Se diseñó una **interfaz gráfica** con `Tkinter` para gestionar la simulación visualmente.
- Se agregó un **modo consola** para pruebas de rendimiento sin la interfaz gráfica.
- Se implementó una **barra de progreso** para simular la duración de la carrera.
- Se permite seleccionar **diferentes etapas** y condiciones de carrera.

---

## 📊 **Diagrama de Clases**
El siguiente diagrama representa la estructura de clases y sus relaciones en el proyecto:

```mermaid
classDiagram
    class Persona {
        + nombre: str
        + cedula: str
    }

    class Ciclista {
        + identificador: str
        + contextura: str
        + especialidad: str
        + tiempo: float
        + get_identificador()
        + set_tiempo()
        + imprimir_tipo()
    }

    class Escuadron {
        + nombre: str
        + pais: str
        + ciclistas: list
        + agregar_ciclista()
        + mostrar_ciclistas()
    }

    class Gestor {
        + escuadron1: Escuadron
        + escuadron2: Escuadron
        + escuadron3: Escuadron
        + iniciar_carrera()
    }

    class Vista {
        + iniciar_interfaz()
    }

    Persona <|-- Ciclista
    Escuadron "1" *-- "6" Ciclista
    Gestor "1" *-- "3" Escuadron
    Gestor "1" *-- "1" Vista



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
