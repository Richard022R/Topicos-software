import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def mostrar_pantalla_mantenimiento (root):
    # Limpiar la ventana principal
    for widget in root.winfo_children():
        widget.destroy()