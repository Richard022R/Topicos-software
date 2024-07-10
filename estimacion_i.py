import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def mostrar_pantalla_estimacion(root):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crear un frame para centrar el contenido
    frame = ttk.Frame(root, padding="20")
    frame.pack(expand=True, fill='both')

    # Etiqueta de título
    titulo_label = ttk.Label(frame, text="Valores del Proyecto a Estimar", font=("Helvetica", 18, "bold"))
    titulo_label.grid(row=0, column=1, columnspan=3, pady=10)

    # Costo hombre-mes promedio con botón "Etapas"
    promedio_label = ttk.Label(frame, text="Costo hombre-mes promedio", font=("Helvetica", 12))
    promedio_label.grid(row=1, column=0, sticky='e', pady=5)

    etapas_button = ttk.Button(frame, text="Etapas")
    etapas_button.grid(row=1, column=1, pady=5, padx=(5, 20))

    # Valor CPM
    cpm_label = ttk.Label(frame, text="Valor CPM:", font=("Helvetica", 12))
    cpm_label.grid(row=1, column=2, sticky='e', pady=5)
    cpm_entry = ttk.Entry(frame, width=20)
    cpm_entry.grid(row=1, column=3, pady=5)

    # Ingrese líneas de código (KLOC)
    kloc_label = ttk.Label(frame, text="Ingrese líneas de código (KLOC)", font=("Helvetica", 12))
    kloc_label.grid(row=2, column=0, sticky='e', pady=5)
    kloc_entry = ttk.Entry(frame, width=20)
    kloc_entry.grid(row=2, column=1, pady=5)

    # Seleccione el tipo de proyecto
    tipo_label = ttk.Label(frame, text="Seleccione el tipo de proyecto", font=("Helvetica", 12))
    tipo_label.grid(row=3, column=0, sticky='e', pady=5)
    tipo_combobox = ttk.Combobox(frame, values=["Orgánico", "Semi-acoplado", "Embebido"], width=18)
    tipo_combobox.grid(row=3, column=1, pady=5)

    # Factores de Cambio
    factores_var = tk.BooleanVar()
    factores_check = ttk.Checkbutton(frame, text="Factores de Cambio", variable=factores_var, command=lambda: activar_botones(factores_var))
    factores_check.grid(row=4, column=0, columnspan=2, pady=10)

    # Factores de Cambio Botones
    factores_frame = ttk.Frame(frame)
    factores_frame.grid(row=5, column=0, columnspan=4, pady=5)
    producto_button = ttk.Button(factores_frame, text="Producto", state="disabled")
    producto_button.grid(row=0, column=0, padx=5)
    plataforma_button = ttk.Button(factores_frame, text="Plataforma", state="disabled")
    plataforma_button.grid(row=0, column=1, padx=5)
    personal_button = ttk.Button(factores_frame, text="Personal", state="disabled")
    personal_button.grid(row=0, column=2, padx=5)
    proyecto_button = ttk.Button(factores_frame, text="Proyecto", state="disabled")
    proyecto_button.grid(row=0, column=3, padx=5)

    botones_factores = [producto_button, plataforma_button, personal_button, proyecto_button]

    # Función para activar/desactivar botones
    def activar_botones(var):
        estado = "normal" if var.get() else "disabled"
        for boton in botones_factores:
            boton.config(state=estado)

    # Botones Limpiar y Estimar
    botones_frame = ttk.Frame(frame)
    botones_frame.grid(row=6, column=0, columnspan=4, pady=20)
    limpiar_button = ttk.Button(botones_frame, text="Limpiar", style="TButton")
    limpiar_button.grid(row=0, column=0, padx=10)
    estimar_button = ttk.Button(botones_frame, text="Estimar", style="TButton")
    estimar_button.grid(row=0, column=1, padx=10)

    # Botón de retroceder con imagen
    image = Image.open("back.png")  # Ruta correcta a la imagen
    image = image.resize((20, 20))
    photo = ImageTk.PhotoImage(image)
    from cocomo_i import mostrar_pantalla_cocomo_81
    boton_retroceder = ttk.Button(frame, image=photo, style="TButton", command=lambda: mostrar_pantalla_cocomo_81(root))
    boton_retroceder.image = photo  # Para que la imagen no se borre
    boton_retroceder.grid(row=0, column=0, pady=10, padx=10, sticky='w')

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Cocomo")
    root.geometry("800x440")
    
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

    mostrar_pantalla_estimacion(root)

    # Hacer que la ventana sea redimensionable
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":  
    main()
