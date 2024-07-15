import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from cocomo_i import mostrar_pantalla_cocomo_81

productos = 0

class FactorCostos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        self.factores = ["RSS", "TBD", "CPR"]
        self.niveles = ["Muy Bajo", "Bajo", "Nominal", "Alto", "Muy Alto", "Extra Alto"]
        self.valores_niveles = {
            "RSS": {
                "Muy Bajo": 0.75, 
                "Bajo": 0.88, 
                "Nominal": 1, 
                "Alto": 1.15, 
                "Muy Alto": 1.40, 
                "Extra Alto": 1
            },
            "TBD": {
                "Muy Bajo": 1,
                "Bajo": 0.94,
                "Nominal": 1,
                "Alto": 1.08,
                "Muy Alto": 1.16,
                "Extra Alto": 1
            },
            "CPR": {
                "Muy Bajo": 0.70,
                "Bajo": 0.85,
                "Nominal": 1,
                "Alto": 1.15,
                "Muy Alto": 1.30,
                "Extra Alto": 1.65
            },
        }
        
        self.selecciones = {factor: tk.StringVar(value="Nominal") for factor in self.factores}
        
        self.setup_ui()
        
    def setup_ui(self):
        # Título y encabezado
        tk.Label(self, text="Producto", font=("Arial", 16)).grid(row=0, column=0, columnspan=7, pady=10)
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
        resultado = 1  # Inicializa el resultado
        producto = 1
        for factor in self.selecciones:
            nivel = self.selecciones[factor].get()
            valor = self.valores_niveles.get(factor, {}).get(nivel, 1)
            resultado *= valor
            producto *= valor
            productos = producto
        with open('producto_factores.txt', 'w') as file:
            file.write(str(productos))
        messagebox.showinfo("Valores Seleccionados", f"Valores: {resultado:.2f}")
        from estimacion_i import mostrar_pantalla_estimacion
        mostrar_pantalla_estimacion(self.parent, resultado)  # Pasa los resultados a la función

def mostrar_pantalla_factores_producto(root):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()
    
    pantalla_factores = FactorCostos(root)
    pantalla_factores.grid(row=0, column=0, padx=10, pady=10)
