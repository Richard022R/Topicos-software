import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from etapas import mostrar_pantalla_etapas


def mostrar_pantalla_estimacion(root, resultado=0,):

    global productos
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

    etapas_button = ttk.Button(frame, text="Etapas", command=lambda: mostrar_pantalla_etapas(root))
    etapas_button.grid(row=1, column=1, pady=5, padx=(5, 20))

    # Valor CPM
    cpm_label = ttk.Label(frame, text="Valor CPM:", font=("Helvetica", 12))
    cpm_label.grid(row=1, column=2, sticky='e', pady=5)
    cpm_entry = ttk.Entry(frame, width=20)
    cpm_entry.grid(row=1, column=3, pady=5)
    with open('etapas_i.txt', 'r') as file:
        etapas_i = file.read()
    
    if etapas_i.strip():  # Verifica si etapas_i no está vacío
        valor_etapas = float(etapas_i)
        print('mostrar etapas: ', etapas_i)
        cpm_entry.insert(0, f"{valor_etapas}")
    else:
        print('El archivo está vacío o contiene solo espacios en blanco.')

    def validate_kloc(*args):
        if kloc_entry_var.get().strip():
            tipo_combobox.config(state="normal")
            with open('kloc_i.txt', 'w') as file:
                file.write(kloc_entry.get())
            print('Se escribio ', kloc_entry)
        else:
            tipo_combobox.config(state="disabled")

    # Asumiendo que 'frame' ya está definido en tu aplicación principal

    # Ingrese líneas de código (KLOC)
    kloc_label = ttk.Label(frame, text="Ingrese líneas de código (KLOC)", font=("Helvetica", 12))
    kloc_label.grid(row=2, column=0, sticky='e', pady=5)
    kloc_entry_var = tk.StringVar()
    kloc_entry_var.trace_add("write", validate_kloc)
    kloc_entry = ttk.Entry(frame, width=20, textvariable=kloc_entry_var)
    kloc_entry.grid(row=2, column=1, pady=5)
    with open('kloc_i.txt', 'r') as file:
        kloc_i = file.read()
    
    if kloc_i.strip():  # Verifica si kloc_i no está vacío
        valor_kloc = float(kloc_i)
        print('mostrar etapas: ', kloc_i)
        kloc_entry.insert(0, f"{valor_kloc}")
    else:
        print('El archivo está vacío o contiene solo espacios en blanco.')

    # Seleccione el tipo de proyecto, mantener desactivado hasta que se ingresen las líneas de código
    tipo_label = ttk.Label(frame, text="Seleccione el tipo de proyecto", font=("Helvetica", 12))
    tipo_label.grid(row=3, column=0, sticky='e', pady=5)
    tipo_combobox = ttk.Combobox(frame, values=["Orgánico", "Moderado", "Embebido"], width=18)
    tipo_combobox.grid(row=3, column=1, pady=5)

    # Factores de Cambio
    factores_var = tk.BooleanVar()
    factores_check = ttk.Checkbutton(frame, text="Factores de Cambio", variable=factores_var, command=lambda: activar_botones(factores_var))
    factores_check.grid(row=4, column=0, columnspan=2, pady=10)

    resultados = []
    # Factores de Cambio Botones
    factores_frame = ttk.Frame(frame)
    factores_frame.grid(row=5, column=0, columnspan=4, pady=5)
    from producto_factores_cocomo_i import mostrar_pantalla_factores_producto
    producto_button = ttk.Button(factores_frame, text="Producto", command=lambda: mostrar_pantalla_factores_producto(root), state="disabled")
    producto_button.grid(row=0, column=0, padx=5)
    resultados.append(resultado)
    from plataforma_factores_cocomo_i import mostrar_pantalla_factores_plataforma
    plataforma_button = ttk.Button(factores_frame, text="Plataforma", command=lambda: mostrar_pantalla_factores_plataforma(root), state="disabled")
    plataforma_button.grid(row=0, column=1, padx=5)
    from personal_factores_cocomo_i import mostrar_pantalla_factores_personal
    personal_button = ttk.Button(factores_frame, text="Personal", command=lambda: mostrar_pantalla_factores_personal(root), state="disabled")
    personal_button.grid(row=0, column=2, padx=5)
    from proyecto_factores_cocomo_i import mostrar_pantalla_factores_proyecto
    proyecto_button = ttk.Button(factores_frame, text="Proyecto", command=lambda: mostrar_pantalla_factores_proyecto(root), state="disabled")
    proyecto_button.grid(row=0, column=3, padx=5)

    botones_factores = [producto_button, plataforma_button, personal_button, proyecto_button]

    with open('personal_factores.txt', 'r') as file:
        contenido_personal = file.read()
    valor_personal = float(contenido_personal)
    print('mostrar personal: ', valor_personal)

    with open('plataforma_factores.txt', 'r') as file:
        contenido_plataforma = file.read()
    valor_plataforma = float(contenido_plataforma)
    print('mostrar plataforma: ', valor_plataforma)

    with open('producto_factores.txt', 'r') as file:
        contenido_producto = file.read()
    valor_producto = float(contenido_producto)
    print('mostrar producto: ', valor_producto)

    with open('proyecto_factores.txt', 'r') as file:
        contenido_proyecto = file.read()
    valor_proyecto = float(contenido_proyecto)
    print('mostrar producto: ', valor_proyecto)

    # Función para activar/desactivar botones
    def activar_botones(var):
        estado = "normal" if var.get() else "disabled"
        for boton in botones_factores:
            boton.config(state=estado)

    # Función para calcular el esfuerzo y tiempo de desarrollo
    def calcular():
        try:
            kloc = float(kloc_entry.get())
            tipo = tipo_combobox.get()
            fec = valor_personal * valor_plataforma * valor_producto * valor_proyecto

            if tipo == "Orgánico":
                esf = 3.2 * (kloc ** 1.05) * fec
                tdes = 2.5 * (esf ** 0.38)
                costo = esf * valor_etapas 
            elif tipo == "Moderado":
                esf = 3.0 * (kloc ** 1.12) * fec
                tdes = 2.5 * (esf ** 0.35)
                costo = esf * valor_etapas 
            elif tipo == "Embebido":
                esf = 2.8 * (kloc ** 1.20) * fec
                tdes = 2.5 * (esf ** 0.32)
                costo = esf * valor_etapas 
            else:
                raise ValueError("Tipo de proyecto no válido")

            resultado_label.config(text=f"Esfuerzo: {esf:.2f} personas-mes\nTiempo de Desarrollo: {tdes:.2f} meses\nCosto de Desarollo: {costo:.2f} soles")
        except ValueError as e:
            resultado_label.config(text=f"Error: {str(e)}")



    # Botones Limpiar y Estimar
    botones_frame = ttk.Frame(frame)
    botones_frame.grid(row=6, column=0, columnspan=4, pady=20)
    limpiar_button = ttk.Button(botones_frame, text="Limpiar", style="TButton", command=lambda: [kloc_entry.delete(0, 'end'), tipo_combobox.set(''), resultado_label.config(text="")])
    limpiar_button.grid(row=0, column=0, padx=10)
    estimar_button = ttk.Button(botones_frame, text="Estimar", style="TButton", command=calcular)
    estimar_button.grid(row=0, column=1, padx=10)

    # Resultado de la estimación
    resultado_label = ttk.Label(frame, text="", font=("Helvetica", 12))
    resultado_label.grid(row=7, column=0, columnspan=4, pady=10)

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