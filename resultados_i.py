import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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

    with open('kloc_i.txt', 'r') as file:
        kloc = file.read()
    valor_kloc = float(kloc)
    print('mostrar kloc: ', valor_kloc)

    with open('tipo_combobox_i.txt', 'r') as file:
        tipo = file.read()
    valor_tipo = tipo
    print('mostrar tipo: ', valor_tipo)
    
    with open('producto_factores.txt', 'r') as file:
        contenido_producto = file.read()
    valor_producto = float(contenido_producto)
    print('mostrar producto: ', valor_producto)
    
    with open('plataforma_factores.txt', 'r') as file:
        contenido_plataforma = file.read()
    valor_plataforma = float(contenido_plataforma)
    print('mostrar plataforma: ', valor_plataforma)

    with open('personal_factores.txt', 'r') as file:
        contenido_personal = file.read()
    valor_personal = float(contenido_personal)
    print('mostrar personal: ', valor_personal)

    with open('etapas_i.txt', 'r') as file:
        contenido_etapas = file.read()
    valor_etapas = float(contenido_etapas)

    with open('proyecto_factores.txt', 'r') as file:
        contenido_proyecto = file.read()
    valor_proyecto = float(contenido_proyecto)
    print('mostrar proyecto: ', valor_proyecto)

    fec = valor_personal * valor_plataforma * valor_producto * valor_proyecto

    if valor_tipo == "Organico":
        esf = 3.2 * (valor_kloc ** 1.05) * fec
        tdes = 2.5 * (esf ** 0.38)
        costo = esf * valor_etapas
    elif tipo == "Moderado":
        esf = 3.0 * (valor_kloc ** 1.12) * fec
        tdes = 2.5 * (esf ** 0.35)
        costo = esf * valor_etapas 
    elif tipo == "Embebido":
        esf = 2.8 * (valor_kloc ** 1.20) * fec
        tdes = 2.5 * (esf ** 0.32)
        costo = esf * valor_etapas

    # Esfuerzo estimado
    esfuerzo_label = ttk.Label(frame, text="Esfuerzo estimado (Persona/Mes):", font=("Helvetica", 12))
    esfuerzo_label.grid(row=1, column=0, padx=(15,1), pady=5)
    esfuerzo_entry = ttk.Entry(frame, width=20)
    esfuerzo_entry.grid(row=1, column=1, pady=1)
    esfuerzo_entry.insert(0, f"{esf:.2f}")

    #Informacion Ecuaciones
    image_info = Image.open("informacion.png")  # Ruta correcta a la imagen
    image_info = image_info.resize((20, 20))
    photo = ImageTk.PhotoImage(image_info)
    from info_esfuerzo_i import mostrar_pantalla_informacion_esfuerzo
    ecuacion_esfuerzo_button = ttk.Button(frame, image=photo, style="TButton", command=lambda: mostrar_pantalla_informacion_esfuerzo(root))
    ecuacion_esfuerzo_button.image = photo  # Para que la imagen no se borre
    ecuacion_esfuerzo_button.grid(row=1, column=2, pady=1, sticky='w')

    # Tiempo estimado de desarrollo
    tiempo_label = ttk.Label(frame, text="Tiempo estimado de desarrollo:", font=("Helvetica", 12))
    tiempo_label.grid(row=2, column=0, sticky='e', pady=5)
    tiempo_entry = ttk.Entry(frame, width=20)
    tiempo_entry.grid(row=2, column=1, pady=5)
    tiempo_entry.insert(0, f"{tdes:.2f}")
    #Informacion Ecuaciones
    image_info = Image.open("informacion.png")  # Ruta correcta a la imagen
    image_info = image_info.resize((20, 20))
    photo = ImageTk.PhotoImage(image_info)
    from info_tiempo_i import mostrar_pantalla_informacion_tiempo
    ecuacion_esfuerzo_button = ttk.Button(frame, image=photo, style="TButton", command=lambda: mostrar_pantalla_informacion_tiempo(root))
    ecuacion_esfuerzo_button.image = photo  # Para que la imagen no se borre
    ecuacion_esfuerzo_button.grid(row=2, column=2, pady=1, sticky='w')

    # Costos estimados
    costo_label = ttk.Label(frame, text="Costos estimados: ", font=("Helvetica", 12))
    costo_label.grid(row=3, column=0, sticky='e', pady=5)
    costo_entry = ttk.Entry(frame, width=20)
    costo_entry.grid(row=3, column=1, pady=5)
    costo_entry.insert(0, f"{costo:.2f}")
    #Informacion Ecuaciones
    image_info = Image.open("informacion.png")  # Ruta correcta a la imagen
    image_info = image_info.resize((20, 20))
    photo = ImageTk.PhotoImage(image_info)
    from info_costos_i import mostrar_pantalla_informacion_costos
    ecuacion_esfuerzo_button = ttk.Button(frame, image=photo, style="TButton", command=lambda: mostrar_pantalla_informacion_costos(root))
    ecuacion_esfuerzo_button.image = photo  # Para que la imagen no se borre
    ecuacion_esfuerzo_button.grid(row=3, column=2, pady=5, sticky='w')

    # Otras opciones
    #mas_info_button = ttk.Button(frame, text="Más información")
    #mas_info_button.grid(row=1, column=3, pady=5, padx=(20, 5))

    #configurar_valores_button = ttk.Button(frame, text="Configurar valores")
    #configurar_valores_button.grid(row=1, column=5, pady=5, padx=(50, 5))

    #mantenimiento_button = ttk.Button(frame, text="Mantenimiento")
    #mantenimiento_button.grid(row=2, column=5, pady=5, padx=(50, 5))

    # Botón de guardar
    guardar_button = ttk.Button(frame, text="Guardar")
    guardar_button.grid(row=4, column=1, pady=50)

    # Botón de retroceder con imagen
    image = Image.open("back.png")  # Ruta correcta a la imagen
    image = image.resize((20, 20))
    photo = ImageTk.PhotoImage(image)
    from estimacion_i import mostrar_pantalla_estimacion
    boton_retroceder = ttk.Button(frame, image=photo, style="TButton", command=lambda: mostrar_pantalla_estimacion(root))
    boton_retroceder.image = photo  # Para que la imagen no se borre
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
