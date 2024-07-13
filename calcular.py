import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from cocomo_i import mostrar_pantalla_cocomo_81

class FactorCostos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        self.factores = ["CAN", "EAN", "CPRO", "ESO", "ELP"]
        self.niveles = ["Muy Bajo", "Bajo", "Nominal", "Alto", "Muy Alto", "Extra Alto"]
        self.valores_niveles = {
            "CAN": {
                "Muy Bajo": 1.46, 
                "Bajo": 1.19, 
                "Nominal": 1, 
                "Alto": 0.86, 
                "Muy Alto": 0.71, 
                "Extra Alto": 1
            },
            "EAN": {
                "Muy Bajo": 1.29,
                "Bajo": 1.13,
                "Nominal": 1,
                "Alto": 0.91,
                "Muy Alto": 0.82,
                "Extra Alto": 1
            },
            "CPRO": {
                "Muy Bajo": 1.42,
                "Bajo": 1.17,
                "Nominal": 1,
                "Alto": 0.86,
                "Muy Alto": 0.70,
                "Extra Alto": 1
            },
            "ESO": {
                "Muy Bajo": 1.21,
                "Bajo": 1.12,
                "Nominal": 1,
                "Alto": 0.96,
                "Muy Alto": 1,
                "Extra Alto": 1
            },
            "ELP": {
                "Muy Bajo": 1.14,
                "Bajo": 1.10,
                "Nominal": 1,
                "Alto": 0.95,
                "Muy Alto": 1,
                "Extra Alto": 1
            },
        }
        
        self.selecciones = {factor: tk.StringVar(value="Nominal") for factor in self.factores}
        self.resultados = {}
        
        self.setup_ui()
        
    def setup_ui(self):
        # Título y encabezado
        tk.Label(self, text="Personal", font=("Arial", 16)).grid(row=0, column=0, columnspan=7, pady=10)
        tk.Label(self, text="Niveles", font=("Arial", 12)).grid(row=1, column=1, columnspan=6)
        
        # Encabezados de niveles
        for i, nivel in enumerate(self.niveles, 1):
            tk.Label(self, text=nivel).grid(row=2, column=i)
        
        # Filas de factores y opciones de selección
        for i, factor in enumerate(self.factores, 3):
            tk.Label(self, text=factor).grid(row=i, column=0, sticky='w', padx=10, pady=5)
            for j, nivel in enumerate(self.niveles, 1):
                radio_button = tk.Radiobutton(self, variable=self.selecciones[factor], value=nivel)
                radio_button.grid(row=i, column=j)
        
        # Botones de Cancelar y Guardar
        tk.Button(self, text="Cancelar", command=self.cancelar).grid(row=len(self.factores) + 3, column=2, pady=10)
        tk.Button(self, text="Guardar", command=self.guardar).grid(row=len(self.factores) + 3, column=4, pady=10)
    
    def cancelar(self):
        # Acción al cancelar (limpiar las selecciones o cerrar la ventana)
        for factor in self.selecciones:
            self.selecciones[factor].set("Nominal")
        messagebox.showinfo("Cancelar", "Selecciones canceladas.")
    
    def guardar(self):
        # Acción al guardar (obtener las selecciones y mostrarlas)
        self.resultados = {}
        producto = 1  # Inicializa el producto
        for factor in self.selecciones:
            nivel = self.selecciones[factor].get()
            valor = self.valores_niveles.get(factor, {}).get(nivel, 1)
            self.resultados[factor] = valor
            producto *= valor
        
        # Mostrar cuadro de mensaje con el producto
        messagebox.showinfo("Valores Seleccionados", f"Producto de valores seleccionados: {producto}")
        
        # Llamar a función externa con el producto
        from estimacion_i import mostrar_pantalla_estimacion
        mostrar_pantalla_estimacion(producto)
