import tkinter as tk
from tkinter import messagebox, ttk
import time

class Vista(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("✪ Simulación de Carrera de Ciclistas 🚴")
        self.geometry("700x500")
        self.configure(bg="#282c34")  # Fondo oscuro

        # Estilos modernos
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TNotebook", background="#1e1e1e", foreground="white", borderwidth=0)
        self.style.configure("TNotebook.Tab", background="#3a3f4b", foreground="white", padding=[10, 5])
        self.style.map("TNotebook.Tab", background=[("selected", "#4caf50")])  # Verde al seleccionar

        self.style.configure("TButton", background="#61afef", foreground="white", font=("Arial", 12), padding=5)
        self.style.map("TButton", background=[("active", "#98c379")])  # Verde al presionar

        self.style.configure("TLabel", background="#282c34", foreground="white", font=("Arial", 12))

        # Crear pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Crear los diferentes paneles
        self.panel_creacion_escuadron()
        self.panel_creacion_ciclista()
        self.panel_creacion_carrera()
        self.panel_marcador_final()
        self.panel_fisio()

    def panel_creacion_escuadron(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="☺ Crear Escuadrón")

        ttk.Label(frame, text="Nombre del Escuadrón").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.nombre_escuadron = ttk.Entry(frame, width=30)
        self.nombre_escuadron.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(frame, text="País").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.pais = ttk.Entry(frame, width=30)
        self.pais.grid(row=1, column=1, padx=10, pady=10)

        self.boton_fisio = ttk.Button(frame, text="Añadir Fisio", command=self.agregar_fisio)
        self.boton_fisio.grid(row=2, column=0, columnspan=2, pady=10)

        self.boton_siguiente = ttk.Button(frame, text="➡ Siguiente", command=self.siguiente_pestaña)
        self.boton_siguiente.grid(row=3, column=0, columnspan=2, pady=10)

    def panel_creacion_ciclista(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="☺ Crear Ciclista")

        ttk.Label(frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.nombre_ciclista = ttk.Entry(frame, width=30)
        self.nombre_ciclista.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Cédula").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.cedula_ciclista = ttk.Entry(frame, width=30)
        self.cedula_ciclista.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(frame, text="Identificador").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.identificador = ttk.Entry(frame, width=30)
        self.identificador.grid(row=2, column=1, padx=10, pady=10)

        self.boton_agregar_ciclista = ttk.Button(frame, text="✔ Añadir Ciclista", command=self.agregar_ciclista)
        self.boton_agregar_ciclista.grid(row=3, column=0, columnspan=2, pady=10)

    def panel_creacion_carrera(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="✪ Carrera")

        ttk.Label(frame, text="Seleccione la etapa").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.tipo_etapa = ttk.Combobox(frame, values=["Montaña", "Llano con curvas", "Semi llano", "De un solo día", "Llano en recta"], width=27)
        self.tipo_etapa.grid(row=0, column=1, padx=10, pady=10)

        self.boton_iniciar_carrera = ttk.Button(frame, text="✪ Iniciar Carrera", command=self.iniciar_carrera)
        self.boton_iniciar_carrera.grid(row=1, column=0, columnspan=2, pady=10)

        self.progress_bar = ttk.Progressbar(frame, orient='horizontal', length=300, mode='determinate')
        self.progress_bar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def panel_marcador_final(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="✪ Resultado")

        ttk.Label(frame, text="Ganador: ").grid(row=0, column=0, padx=10, pady=10)
        self.marcador_ganador = ttk.Label(frame, text="Aún no hay ganador")
        self.marcador_ganador.grid(row=0, column=1, padx=10, pady=10)

        self.boton_salir = ttk.Button(frame, text="✘ Salir", command=self.quit)
        self.boton_salir.grid(row=1, column=0, columnspan=2, pady=10)

    def panel_fisio(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="✪ Fisio")

        ttk.Label(frame, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        self.nombre_fisio = ttk.Entry(frame, width=30)
        self.nombre_fisio.grid(row=0, column=1, padx=10, pady=10)

        self.boton_guardar_fisio = ttk.Button(frame, text="★ Guardar Fisio", command=self.guardar_fisio)
        self.boton_guardar_fisio.grid(row=1, column=0, columnspan=2, pady=10)

    def agregar_fisio(self):
        messagebox.showinfo("Info", "Fisio añadido correctamente")

    def agregar_ciclista(self):
        messagebox.showinfo("Info", "Ciclista añadido correctamente")

    def iniciar_carrera(self):
        self.progress_bar["value"] = 0
        self.update_idletasks()
        for i in range(0, 101, 10):
            time.sleep(0.3)
            self.progress_bar["value"] = i
            self.update_idletasks()
        self.progress_bar["value"] = 100
        self.marcador_ganador.config(text="✪ ¡Carrera Finalizada!")

    def guardar_fisio(self):
        messagebox.showinfo("Info", "Fisio guardado correctamente")

    def siguiente_pestaña(self):
        self.notebook.select(self.notebook.index(self.notebook.select()) + 1)

if __name__ == "__main__":
    app = Vista()
    app.mainloop()
