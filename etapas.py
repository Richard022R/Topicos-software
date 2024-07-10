import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class CostEstimator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        self.etapas = ["Requerimientos", "Planificación", "Análisis", "Diseño", "Programación", "Pruebas", "Implantación"]
        self.etapa_var = tk.StringVar()
        self.esfuerzo_var = tk.StringVar()
        self.costo_var = tk.StringVar()
        
        self.etapa_var.set(self.etapas[0])
        
        self.setup_ui()
        
    def setup_ui(self):
        # Crear y posicionar widgets
        etapa_label = ttk.Label(self, text="Etapa:")
        etapa_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.etapa_option = ttk.OptionMenu(self, self.etapa_var, *self.etapas)
        self.etapa_option.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        esfuerzo_label = ttk.Label(self, text="Esfuerzo Porcentual (%):")
        esfuerzo_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.esfuerzo_entry = ttk.Entry(self, textvariable=self.esfuerzo_var)
        self.esfuerzo_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        costo_label = ttk.Label(self, text="Costo por Etapa:")
        costo_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        self.costo_entry = ttk.Entry(self, textvariable=self.costo_var)
        self.costo_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        agregar_button = ttk.Button(self, text="Agregar", command=self.agregar_etapa)
        agregar_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")
        
        # Tabla
        columns = ("Etapa", "Esfuerzo (%)", "Costo")
        self.tree = ttk.Treeview(self, columns=columns, show='headings', selectmode='browse')
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        guardar_button = ttk.Button(self, text="Guardar", command=self.guardar)
        guardar_button.grid(row=5, column=1, padx=10, pady=10, sticky="e")
    
    def agregar_etapa(self):
        etapa = self.etapa_var.get()
        esfuerzo = self.esfuerzo_var.get()
        costo = self.costo_var.get()
        
        if not esfuerzo.isdigit() or not costo.isdigit():
            messagebox.showerror("Error", "Esfuerzo y Costo deben ser números.")
            return
        
        esfuerzo = int(esfuerzo)
        costo = int(costo)
        
        if esfuerzo < 1 or esfuerzo > 100:
            messagebox.showerror("Error", "Esfuerzo debe ser un porcentaje entre 1 y 100.")
            return
        
        total_esfuerzo = sum(int(self.tree.item(item, 'values')[1]) for item in self.tree.get_children())
        
        if total_esfuerzo + esfuerzo > 100:
            messagebox.showerror("Error", "El esfuerzo total no puede exceder el 100%.")
            return
        
        self.tree.insert("", "end", values=(etapa, esfuerzo, costo))
        self.esfuerzo_var.set("")
        self.costo_var.set("")
    
    def guardar(self):
        total_costo = sum((int(item[1]) / 100) * int(item[2]) for item in [self.tree.item(item, 'values') for item in self.tree.get_children()])
        messagebox.showinfo("Costo Promedio", f"Costo Hombre Promedio Mes: {total_costo:.2f}")
        from estimacion_i import mostrar_pantalla_estimacion
        mostrar_pantalla_estimacion(self.parent, total_costo)

def mostrar_pantalla_etapas(root):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()
    
    pantalla_etapas = CostEstimator(root)
    pantalla_etapas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Software de Estimación de Costos")
    root.geometry("600x400")
    
    mostrar_pantalla_etapas(root)
    
    root.mainloop()
