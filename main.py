import tkinter as tk
from tkinter import ttk
from cocomo_i import mostrar_pantalla_cocomo_81
from cocomo_ii import mostrar_pantalla_cocomo_ii

def mostrar_pantalla_principal(root):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crear un frame para centrar el contenido
    frame = ttk.Frame(root, padding="20")
    frame.pack(expand=True, fill='both')

    # Etiqueta de bienvenida
    bienvenida_label = ttk.Label(frame, text="Bienvenido a mi software de estimación", font=("Helvetica", 24, "bold"))
    bienvenida_label.pack(pady=30)

    # Crear un frame para los botones y centrarlos
    button_frame = ttk.Frame(frame)
    button_frame.pack(expand=True, pady=20)

    # Botón para COCOMO I
    cocomo_81_button = ttk.Button(button_frame, text="COCOMO I", command=lambda: mostrar_pantalla_cocomo_81(root), style="TButton")
    cocomo_81_button.pack(pady=10, padx=10)

    # Botón para COCOMO II
    cocomo_ii_button = ttk.Button(button_frame, text="COCOMO II", command=lambda: mostrar_pantalla_cocomo_ii(root), style="TButton")
    cocomo_ii_button.pack(pady=10, padx=10)

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Cocomo")
    root.geometry("800x540")

    # limpiar todos los archivos
    with open('kloc_i.txt', 'w') as file:
        file.write('')
    with open('etapas_i.txt', 'w') as file:
        file.write('')
    with open('costo_i.txt', 'w') as file:
        file.write('')
    with open('esfuerzo_i', 'w') as file:
        file.write('')
    
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
