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
    frame.pack(expand=True)

    # Etiqueta de bienvenida
    bienvenida_label = ttk.Label(frame, text="Bienvenido a mi software de estimación", font=("Arial", 20))
    bienvenida_label.pack(pady=20)

    # Botón para COCOMO I
    cocomo_81_button = ttk.Button(frame, text="COCOMO I", command=lambda: mostrar_pantalla_cocomo_81(root))
    cocomo_81_button.pack(pady=10)

    # Botón para COCOMO II
    cocomo_ii_button = ttk.Button(frame, text="COCOMO II", command=lambda: mostrar_pantalla_cocomo_ii(root))
    cocomo_ii_button.pack(pady=10)

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("CocoYunobi maricon")
    root.geometry("600x400")

    mostrar_pantalla_principal(root)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
