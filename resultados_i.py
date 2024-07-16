import tkinter as tk
from tkinter import ttk

def mostrar_pantalla_resultados(root, esf=0, tdes=0, costo=0):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crear un frame para centrar el contenido
    frame = ttk.Frame(root, padding="20")
    frame.pack(expand=True, fill='both')

    # Etiqueta de título
    titulo_label = ttk.Label(frame, text="Proyecto Estimado", font=("Helvetica", 18, "bold"))
    titulo_label.grid(row=0, column=1, columnspan=3, pady=10)

    # Esfuerzo estimado
    esfuerzo_label = ttk.Label(frame, text="Mostrar el esfuerzo estimado", font=("Helvetica", 12))
    esfuerzo_label.grid(row=1, column=0, sticky='e', pady=5)
    esfuerzo_entry = ttk.Entry(frame, width=20)
    esfuerzo_entry.grid(row=1, column=1, pady=5)
    esfuerzo_entry.insert(0, f"{esf:.2f}")

    # Tiempo estimado de desarrollo
    tiempo_label = ttk.Label(frame, text="Tiempo estimado de desarrollo", font=("Helvetica", 12))
    tiempo_label.grid(row=2, column=0, sticky='e', pady=5)
    tiempo_entry = ttk.Entry(frame, width=20)
    tiempo_entry.grid(row=2, column=1, pady=5)
    tiempo_entry.insert(0, f"{tdes:.2f}")

    # Costos estimados
    costo_label = ttk.Label(frame, text="Costos estimados", font=("Helvetica", 12))
    costo_label.grid(row=3, column=0, sticky='e', pady=5)
    costo_entry = ttk.Entry(frame, width=20)
    costo_entry.grid(row=3, column=1, pady=5)
    costo_entry.insert(0, f"{costo:.2f}")

    # Otras opciones
    mas_info_button = ttk.Button(frame, text="Más información")
    mas_info_button.grid(row=1, column=3, pady=5, padx=(20, 5))

    configurar_valores_button = ttk.Button(frame, text="Configurar valores")
    configurar_valores_button.grid(row=2, column=3, pady=5, padx=(20, 5))

    mantenimiento_button = ttk.Button(frame, text="Mantenimiento")
    mantenimiento_button.grid(row=3, column=3, pady=5, padx=(20, 5))

    # Botón de guardar
    guardar_button = ttk.Button(frame, text="Guardar")
    guardar_button.grid(row=4, column=1, pady=20)

    # Botón de retroceder con imagen
    image = tk.PhotoImage(file="back.png")  # Ruta correcta a la imagen
    from cocomo_i import mostrar_pantalla_cocomo_81
    boton_retroceder = ttk.Button(frame, image=image, style="TButton", command=lambda: mostrar_pantalla_cocomo_81(root))
    boton_retroceder.image = image  # Para que la imagen no se borre
    boton_retroceder.grid(row=0, column=0, pady=10, padx=10, sticky='w')

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Proyecto Estimado")
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

    mostrar_pantalla_resultados(root)

    # Hacer que la ventana sea redimensionable
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":  
    main()
