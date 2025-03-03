import tkinter as tk
from tkinter import messagebox, ttk

class Vista(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulación de Carrera de Ciclistas")
        self.geometry("600x400")

        # Crear pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        # Crear los diferentes paneles
        self.panel_creacion_escuadron()
        self.panel_creacion_ciclista()
        self.panel_creacion_carrera()
        self.panel_marcador_final()
        self.panel_masajista()

    def panel_creacion_escuadron(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Creación Escuadrón")

        ttk.Label(frame, text="Nombre del Escuadrón").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_escuadron = ttk.Entry(frame)
        self.nombre_escuadron.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="País").grid(row=1, column=0, padx=5, pady=5)
        self.pais = ttk.Entry(frame)
        self.pais.grid(row=1, column=1, padx=5, pady=5)

        self.boton_masajista = ttk.Button(frame, text="Añadir Masajista", command=self.agregar_masajista)
        self.boton_masajista.grid(row=2, column=0, padx=5, pady=5)

        self.boton_siguiente = ttk.Button(frame, text="Siguiente", command=self.siguiente_pestaña)
        self.boton_siguiente.grid(row=2, column=1, padx=5, pady=5)

    def panel_creacion_ciclista(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Creación Ciclista")

        ttk.Label(frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_ciclista = ttk.Entry(frame)
        self.nombre_ciclista.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Cédula").grid(row=1, column=0, padx=5, pady=5)
        self.cedula_ciclista = ttk.Entry(frame)
        self.cedula_ciclista.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Identificador").grid(row=2, column=0, padx=5, pady=5)
        self.identificador = ttk.Entry(frame)
        self.identificador.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Especialidad").grid(row=3, column=0, padx=5, pady=5)
        self.especialidad = ttk.Combobox(frame, values=["Montaña", "Llano con curvas", "Semi llano", "De un solo día", "Llano en recta"])
        self.especialidad.grid(row=3, column=1, padx=5, pady=5)

        self.boton_agregar_ciclista = ttk.Button(frame, text="Añadir Ciclista", command=self.agregar_ciclista)
        self.boton_agregar_ciclista.grid(row=4, column=0, padx=5, pady=5)

        self.boton_crear_escuadron = ttk.Button(frame, text="Crear Escuadrón", command=self.crear_escuadron)
        self.boton_crear_escuadron.grid(row=4, column=1, padx=5, pady=5)

    def panel_creacion_carrera(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Creación Carrera")

        ttk.Label(frame, text="Seleccione la etapa").grid(row=0, column=0, padx=5, pady=5)
        self.tipo_etapa = ttk.Combobox(frame, values=["Montaña", "Llano con curvas", "Semi llano", "De un solo día", "Llano en recta"])
        self.tipo_etapa.grid(row=0, column=1, padx=5, pady=5)

        self.boton_iniciar_carrera = ttk.Button(frame, text="Iniciar Carrera", command=self.iniciar_carrera)
        self.boton_iniciar_carrera.grid(row=1, column=0, padx=5, pady=5)

        self.boton_mostrar_marcador = ttk.Button(frame, text="Mostrar Marcador", command=self.mostrar_marcador)
        self.boton_mostrar_marcador.grid(row=1, column=1, padx=5, pady=5)

        self.progress_bar = ttk.Progressbar(frame, orient='horizontal', length=300, mode='determinate')
        self.progress_bar.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    def panel_marcador_final(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Marcador Final")

        ttk.Label(frame, text="Ganador: ").grid(row=0, column=0, padx=5, pady=5)
        self.marcador_ganador = ttk.Label(frame, text="")
        self.marcador_ganador.grid(row=0, column=1, padx=5, pady=5)

        self.boton_salir = ttk.Button(frame, text="Salir", command=self.quit)
        self.boton_salir.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def panel_masajista(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Masajista")

        ttk.Label(frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_masajista = ttk.Entry(frame)
        self.nombre_masajista.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Cédula").grid(row=1, column=0, padx=5, pady=5)
        self.cedula_masajista = ttk.Entry(frame)
        self.cedula_masajista.grid(row=1, column=1, padx=5, pady=5)

        self.boton_guardar_masajista = ttk.Button(frame, text="Guardar Masajista", command=self.guardar_masajista)
        self.boton_guardar_masajista.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def agregar_masajista(self):
        messagebox.showinfo("Info", "Masajista añadido correctamente")

    def agregar_ciclista(self):
        messagebox.showinfo("Info", "Ciclista añadido correctamente")

    def crear_escuadron(self):
        messagebox.showinfo("Info", "Escuadrón creado correctamente")

    def iniciar_carrera(self):
        self.progress_bar.start(10)

    def mostrar_marcador(self):
        self.marcador_ganador.config(text="Equipo X - Ganador")

    def guardar_masajista(self):
        messagebox.showinfo("Info", "Masajista guardado correctamente")

    def siguiente_pestaña(self):
        self.notebook.select(self.notebook.index(self.notebook.select()) + 1)

if __name__ == "__main__":
    app = Vista()
    app.mainloop()
