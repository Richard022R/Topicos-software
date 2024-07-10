import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, Frame, Scrollbar
from PIL import Image, ImageTk

def mostrar_pantalla_informacion(root):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crear un frame para contener el canvas y la scrollbar
    container = ttk.Frame(root)
    container.pack(expand=True, fill='both')

    # Crear un canvas
    canvas = tk.Canvas(container, borderwidth=0, background="#F0F0F0")
    canvas.pack(side="left", fill="both", expand=True)

    # Agregar una scrollbar vertical al canvas
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configurar el canvas para usar la scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Crear un frame dentro del canvas
    frame = ttk.Frame(canvas, padding="50")
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Actualizar la región scrollable del canvas
    frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    from cocomo_i import mostrar_pantalla_cocomo_81

    # Botón de retroceder con imagen
    try:
        image = Image.open("back.png")  # Ruta correcta a la imagen
        image = image.resize((20, 20))
        photo = ImageTk.PhotoImage(image)
    except Exception as e:
        print("Error loading image:", e)
        photo = None

    if photo:
        boton_retroceder = ttk.Button(frame, image=photo, command=lambda: mostrar_pantalla_cocomo_81(root))
        boton_retroceder.image = photo  # Para que la imagen no se borre
        boton_retroceder.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    else:
        boton_retroceder = ttk.Button(frame, text="Volver", command=lambda: mostrar_pantalla_cocomo_81(root))
        boton_retroceder.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    # Etiqueta de título
    titulo_label = ttk.Label(frame, text="Información de COCOMO I", font=("Helvetica", 24, "bold"))
    titulo_label.grid(row=0, column=0, sticky="w", padx=70, pady=10)
    
    # Descripción de COCOMO I
    descripcion = ("COCOMO (Constructive Cost Model) es un modelo de estimación de costos de software "
                   "desarrollado por Barry Boehm en 1981. COCOMO I es la primera versión de este modelo y "
                   "se utiliza para predecir el esfuerzo, el costo y el tiempo de desarrollo de un proyecto de software "
                   "en función del tamaño del código fuente.\n\n"
                   "El modelo COCOMO I se divide en tres submodelos:\n"
                   "1. Básico: Proporciona una estimación rápida y de bajo costo del esfuerzo de desarrollo.\n"
                   "2. Intermedio: Considera un conjunto de atributos del proyecto (factores de costo) además del tamaño del software.\n"
                   "3. Avanzado: Incluye una evaluación detallada de los atributos del proyecto y una estimación del esfuerzo para cada fase del ciclo de vida del software.\n\n"
                   "Los resultados de COCOMO I se expresan en términos de la cantidad de personas-mes necesarias para completar el proyecto y el tiempo de desarrollo en meses.\n\n"
                   "Las fórmulas que el COCOMO I trabaja son las siguientes:")

    descripcion_label = ttk.Label(frame, text=descripcion, wraplength=700, justify="left", font=("Helvetica", 12))
    descripcion_label.grid(pady=20)

    # Imagen en la parte inferior
    try:
        bottom_image = Image.open("cocomo_i.png")
        bottom_image = bottom_image.resize((656, 242))  # Ajustar el tamaño de la imagen si es necesario
        photo_bottom = ImageTk.PhotoImage(bottom_image)
        bottom_label = ttk.Label(frame, image=photo_bottom)
        bottom_label.image = photo_bottom
        bottom_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    except Exception as e:
        print("Error loading bottom image:", e)

def mostrar_pantalla_principal(root):       
    from main import mostrar_pantalla_principal
    mostrar_pantalla_principal(root)

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

    mostrar_pantalla_principal(root)

    # Hacer que la ventana sea redimensionable
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":  
    main()