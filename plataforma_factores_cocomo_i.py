import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from cocomo_i import mostrar_pantalla_cocomo_81

productos = 0

class FactorCostos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        self.factores = ["RTE", "RMP", "VMC", "TRC"]
        self.niveles = ["Muy Bajo", "Bajo", "Nominal", "Alto", "Muy Alto", "Extra Alto"]
        self.valores_niveles = {
            "RTE": {
                "Muy Bajo": 1, 
                "Bajo": 1, 
                "Nominal": 1, 
                "Alto": 1.11, 
                "Muy Alto": 1.30, 
                "Extra Alto": 1.66
            },
            "RMP": {
                "Muy Bajo": 1,
                "Bajo": 1,
                "Nominal": 1,
                "Alto": 1.06,
                "Muy Alto": 1.30,
                "Extra Alto": 1.58
            },
            "VMC": {
                "Muy Bajo": 1,
                "Bajo": 0.87,
                "Nominal": 1,
                "Alto": 1.15,
                "Muy Alto": 1.30,
                "Extra Alto": 1
            },
            "TRC": {
                "Muy Bajo": 1,
                "Bajo": 0.87,
                "Nominal": 1,
                "Alto": 1.07,
                "Muy Alto": 1.15,
                "Extra Alto": 1
            },
        }
        
        self.selecciones = {factor: tk.StringVar(value="Nominal") for factor in self.factores}
        
        self.setup_ui()
        
    def setup_ui(self):
        # Título y encabezado
        tk.Label(self, text="Plataforma (Computador)", font=("Arial", 16)).grid(row=0, column=0, columnspan=7, pady=10)
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
        with open('personal_factores.txt', 'w') as file:
            file.write(str(productos))
        messagebox.showinfo("Valores Seleccionados", f"Valores: {resultado}")
        from estimacion_i import mostrar_pantalla_estimacion
        mostrar_pantalla_estimacion(self.parent, resultado)  # Pasa los resultados a la función

def mostrar_pantalla_estimacion(root, resultados):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()
    
    # Aquí puedes usar los valores de 'resultados' para mostrarlos o procesarlos en la interfaz de estimación
    tk.Label(root, text="Interfaz de Estimación", font=("Arial", 16)).pack(pady=20)
    
    # Mostrar los valores obtenidos
    for factor, valor in resultados.items():
        tk.Label(root, text=f"{factor}: {valor}", font=("Arial", 12)).pack(pady=5)
    
    # Aquí puedes agregar más widgets y lógica para la pantalla de estimación

def mostrar_pantalla_factores_plataforma(root):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()
    
    pantalla_factores = FactorCostos(root)
    pantalla_factores.grid(row=0, column=0, padx=10, pady=10)

def mostrar_pantalla_plataforma(root):
    mostrar_pantalla_factores_plataforma(root)

def mostrar_pantalla_principal(root):       
    # Aquí se puede definir la función para mostrar la pantalla principal
    pass

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Cocomo")
    root.geometry("800x540")
    
    # Configurar estilos
    style = ttk.Style()
    style.theme_use("clam")  # Puedes probar otros temas como 'default', 'alt', 'clam', 'classic'
    
    # Colores y estilo para los botones
    style.configure("TButton",
                    font=("Helvetica", 16),
                    padding=10,
                    borderwidth=2,
                    relief="raised",
                    background="#4CAF50",  # Color del fondo
                    foreground="white")    # Color del texto
    style.map("TButton",
              background=[('active', '#45a049')])  # Color al hacer hover

    # Colores para la ventana principal
    root.configure(bg="#F0F0F0")

    mostrar_pantalla_principal(root)

    # Hacer que la ventana principal sea resizable
    root.resizable(True, True)

    # Iniciar el bucle principal
    root.mainloop()