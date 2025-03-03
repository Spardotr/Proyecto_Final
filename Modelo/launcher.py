from gestor import Gestor
from vista import Vista

def main():
    gestor = Gestor()
    vista = Vista()

    print("¿Quieres usar la interfaz gráfica? (sí/no)")
    opcion = input().strip().lower()

    if opcion == "si" or opcion == "sí":
        vista.mainloop()  # Inicia la interfaz gráfica
    else:
        print("Modo consola activado: Creando escuadrones con ciclistas...")

        # 🔹 Creación de Escuadrones
        gestor.escuadron1 = gestor.crear_escuadron("Equipo A", "Colombia")
        gestor.escuadron2 = gestor.crear_escuadron("Equipo B", "España")
        gestor.escuadron3 = gestor.crear_escuadron("Equipo C", "Francia")

        # 🔹 Agregar ciclistas con distintos roles a cada escuadrón
        equipos_roles = {
                    "A": ["Escalador", "Escalador", "Rodador", "Embalador", "Gregario", "Contrarrelojista"],
                    "B": ["Escalador", "Rodador", "Embalador", "Gregario", "Contrarrelojista", "Contrarrelojista"],
                    "C": ["Escalador", "Rodador", "Embalador", "Embalador", "Gregario", "Clasicómano"]
                }

                # 🔹 Agregar ciclistas a cada equipo con identificador y cédula única
        for escuadron, equipo in zip([gestor.escuadron1, gestor.escuadron2, gestor.escuadron3], equipos_roles.keys()):
            for i, rol in enumerate(equipos_roles[equipo]):
                nombre = f"Ciclista_{rol}_{equipo}"
                cedula = 1011088500 + i  # Cédula única por ciclista
                identificador = f"{i+1}{equipo}"
                escuadron.agregar_ciclista(identificador, nombre, rol, cedula)
                print(f"✔ {nombre} agregado al escuadrón {equipo}.")
        print("✔ Escuadrones completos y listos para la carrera.")

        # 🔹 Configurar la carrera
        print("\nSelecciona el tipo de etapa:")
        print("1. Montaña")
        print("2. Llano con curvas")
        print("3. Semi llano")
        print("4. De un solo día")
        print("5. Llano en recta")

        etapa_opcion = input("Elige el número de la etapa: ").strip()

        etapas = {
            "1": "Montaña",
            "2": "Llano con curvas",
            "3": "Semi llano",
            "4": "De un solo día",
            "5": "Llano en recta"
        }

        tipo_etapa = etapas.get(etapa_opcion, "Montaña")  # Si la entrada es incorrecta, usa "Montaña" por defecto

        print(f"\n🏁 Iniciando carrera en etapa: {tipo_etapa} 🏁\n")

        # 🔹 Iniciar la carrera con la etapa seleccionada
        gestor.iniciar_carrera(tipo_etapa)

if __name__ == "__main__":
    main()
