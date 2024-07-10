import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from estimacion_i import mostrar_pantalla_estimacion
from mantenimiento_i import mostrar_pantalla_mantenimiento   
from informacion_i import mostrar_pantalla_informacion    

def mostrar_pantalla_cocomo_81(root):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crear un frame para centrar el contenido
    frame = ttk.Frame(root, padding="20")
    frame.pack(expand=True, fill='both')

    # Etiqueta de título
    titulo_label = ttk.Label(frame, text="Estimación con COCOMO I", font=("Helvetica", 24, "bold"))
    titulo_label.pack(pady=20)

    # Crear un frame para los botones y centrarlos
    button_frame = ttk.Frame(frame)
    button_frame.pack(expand=True, pady=20)

    # Botón para Iniciar estimación
    boton_estimacion = ttk.Button(button_frame, text="Iniciar estimación", style="TButton", command=lambda: mostrar_pantalla_estimacion(root))
    boton_estimacion.pack(pady=10, padx=10)

    # Botón para Calculo del mantenimiento
    boton_mantenimiento = ttk.Button(button_frame, text="Calculo del mantenimiento", style="TButton", command=lambda: mostrar_pantalla_mantenimiento(root))
    boton_mantenimiento.pack(pady=10, padx=10)

    # Botón para Información
    boton_informacion = ttk.Button(button_frame, text="Información", style="TButton", command=lambda: mostrar_pantalla_informacion(root))
    boton_informacion.pack(pady=10, padx=10)

    # Botón de retroceder con imagen
    image = Image.open("back.png")
    image = image.resize((20, 20))
    photo = ImageTk.PhotoImage(image)
    boton_retroceder = ttk.Button(frame, image=photo, style="TButton", command=lambda: mostrar_pantalla_principal(root))
    boton_retroceder.image = photo  # Para que la imagen no se borre
    boton_retroceder.pack(pady=10)

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