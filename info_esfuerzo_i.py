import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def mostrar_pantalla_informacion_esfuerzo(root):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crear un frame para centrar el contenido
    frame = ttk.Frame(root, padding="20")
    frame.pack(expand=True, fill='both')

    # Botón de retroceder con imagen
    image = Image.open("back.png")  # Ruta correcta a la imagen
    image = image.resize((20, 20))
    photo = ImageTk.PhotoImage(image)
    from resultados_i import mostrar_pantalla_resultados
    boton_retroceder = ttk.Button(frame, image=photo, style="TButton", command=lambda: mostrar_pantalla_resultados(root))
    boton_retroceder.image = photo  # Para que la imagen no se borre
    boton_retroceder.grid(row=0, column=0, pady=10, padx=5, sticky='w')

    # Etiqueta de título
    titulo_label = ttk.Label(frame, text="Ecuaciones para Esfuerzo Estimado", font=("Helvetica", 18, "bold"))
    titulo_label.grid(row=0, column=1, pady=10, sticky="w")

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
    elif valor_tipo == "Moderado":
        esf = 3.0 * (valor_kloc ** 1.12) * fec
        tdes = 2.5 * (esf ** 0.35)
        costo = esf * valor_etapas 
    elif valor_tipo == "Embebido":
        esf = 2.8 * (valor_kloc ** 1.20) * fec
        tdes = 2.5 * (esf ** 0.32)
        costo = esf * valor_etapas

    if valor_tipo == "Organico":
        descripcion = ("Tipo de Proyecto: Orgánico\n\n"
                       "ESF = 3.2 (KLDC)^1.05 * FEC\n"
                       f"ESF = 3.2 ({valor_kloc:.2f})^1.05\n"
                       f"           * {valor_producto:.2f} * {valor_plataforma:.2f} * {valor_personal:.2f} * {valor_proyecto:.2f}\n"
                       f"ESF = 3.2 ({valor_kloc**1.05:.2f}) * {fec:.2f}\n"
                       f"ESF = {esf:.2f}"

        )
    elif valor_tipo == "Moderado":
        descripcion = ("Tipo de Proyecto: Moderado\n\n"
                       "ESF = 3.0 (KLDC)^1.12 * FEC\n"
                       f"ESF = 3.0 ({valor_kloc:.2f})^1.12\n"
                       f"           * {valor_producto:.2f} * {valor_plataforma:.2f} * {valor_personal:.2f} * {valor_proyecto:.2f}\n"
                       f"ESF = 3.0 ({valor_kloc**1.12:.2f}) * {fec:.2f}\n"
                       f"ESF = {esf:.2f}"
        )
    elif valor_tipo == "Embebido":
        descripcion = ("Tipo de Proyecto: Embebido\n\n"
                       "ESF = 2.8 (KLDC)^1.20 * FEC\n"
                       f"ESF = 2.8 ({valor_kloc:.2f})^1.20\n"
                       f"           * {valor_producto:.2f} * {valor_plataforma:.2f} * {valor_personal:.2f} * {valor_proyecto:.2f}\n"
                       f"ESF = 2.8 ({valor_kloc**1.20:.2f}) * {fec:.2f}\n"
                       f"ESF = {esf:.2f}"
        )

    descripcion_label = ttk.Label(frame, text=descripcion, wraplength=700, justify="left", font=("Helvetica", 13))
    descripcion_label.grid(pady=20)

    try:
        bottom_image = Image.open("esf_cocomo_inter_i.png")
        bottom_image = bottom_image.resize((300, 142))  # Ajustar el tamaño de la imagen si es necesario
        photo_bottom = ImageTk.PhotoImage(bottom_image)
        bottom_label = ttk.Label(frame, image=photo_bottom)
        bottom_label.image = photo_bottom
        bottom_label.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

    except Exception as e:
        print("Error loading bottom image:", e)

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

    mostrar_pantalla_informacion_esfuerzo(root)

    # Hacer que la ventana sea redimensionable
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":  
    main()
