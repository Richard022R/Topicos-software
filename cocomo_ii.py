import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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

def mostrar_pantalla_cocomo_ii(root):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()
    
    # Crear el nuevo contenido
    titulo_label = ttk.Label(root, text="Estimación con COCOMO II", font=("Arial", 20))
    titulo_label.pack(pady=20)
    
    boton_estimacion = ttk.Button(root, text="Iniciar estimación", command=iniciar_estimacion)
    boton_estimacion.pack(pady=10)
    
    boton_mantenimiento = ttk.Button(root, text="Calculo del mantenimiento", command=calculo_mantenimiento)
    boton_mantenimiento.pack(pady=10)
    
    boton_informacion = ttk.Button(root, text="Información", command=mostrar_informacion)
    boton_informacion.pack(pady=10)
    
    # boton de retroceder con imagen
    image = Image.open("back.png")
    image = image.resize((20, 20))
    photo = ImageTk.PhotoImage(image)
    boton_retroceder = ttk.Button(root, image=photo, command=lambda: mostrar_pantalla_principal(root))
    boton_retroceder.place(x=15, y=15)
    boton_retroceder.image = photo # para que la imagen no se borre

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
