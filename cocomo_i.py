import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def mostrar_pantalla_cocomo_81(root):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()
    
    # Crear el nuevo contenido
    titulo_label = ttk.Label(root, text="Estimación con COCOMO I", font=("Arial", 20))
    titulo_label.pack(pady=20)
    
    boton_estimacion = ttk.Button(root, text="Iniciar estimación", command=iniciar_estimacion)
    boton_estimacion.pack(pady=10)
    
    boton_mantenimiento = ttk.Button(root, text="Calculo del mantenimiento", command=calculo_mantenimiento)
    boton_mantenimiento.pack(pady=10)
    
    boton_informacion = ttk.Button(root, text="Información", command=mostrar_informacion)
    boton_informacion.pack(pady=10)
    
    # Cargar la imagen del icono de retroceder
    back_icon = Image.open("path/to/your/back_icon.png")  # Cambia la ruta a tu icono de retroceso
    back_icon = back_icon.resize((30, 30), Image.ANTIALIAS)
    back_icon = ImageTk.PhotoImage(back_icon)
    
    # Botón de retroceder con icono
    boton_retroceder = ttk.Button(root, image=back_icon, command=lambda: mostrar_pantalla_principal(root))
    boton_retroceder.image = back_icon  # Necesario para que la imagen no sea recolectada por el garbage collector
    boton_retroceder.place(x=10, y=10)

def iniciar_estimacion():
    # Aquí va el código para iniciar la estimación
    pass

def calculo_mantenimiento():
    # Aquí va el código para el cálculo del mantenimiento
    pass

def mostrar_informacion():
    # Aquí va el código para mostrar la información
    pass

def mostrar_pantalla_principal(root):
    # Importar la función desde el main
    from main import mostrar_pantalla_principal
    mostrar_pantalla_principal(root)
