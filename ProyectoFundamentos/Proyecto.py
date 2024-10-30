import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os


fuente = ("Futura Bold Condensed BT", 30)

def cargarImagen(nombre): 
    ruta = os.path.join("imagenes", nombre)
    imagen = ImageTk.PhotoImage(file=ruta)
    return imagen

def VentanaInicio():
    global ventana
    ventana = tk.Tk()
    ventana.title("VENTANA PRINCIPAL")
    ventana.state('zoomed')
    ventana.resizable(width=False, height=False)

    fondoinicio = cargarImagen("fondoi.png")
    Labelfondoinicio = Label(ventana, image=fondoinicio)
    Labelfondoinicio.image = fondoinicio
    Labelfondoinicio.pack()

    boton = Button(ventana, text="INFORMACIÓN", bg='#fc3f02', fg="black", command=lambda: [ventana.withdraw(), VentanaInfo()])
    boton.pack()
    boton.place(relx=0.75, rely=0.7, anchor='center')
    boton.config(height=4, width=20)
    boton['font'] = fuente

    cierrainicio = Button(ventana, text="X", bg="red", fg="black", command=ventana.destroy)
    cierrainicio.pack(pady=50)
    cierrainicio.place(relx=0.95, rely=0.09, anchor='center')
    cierrainicio.config(height=2, width=7)
    cierrainicio['font'] = fuente

    ventana.mainloop()

def VentanaInfo():
    global ventana_info
    ventana_info = Toplevel(ventana)  
    ventana_info.title("VENTANA INFORMACIÓN")
    ventana_info.state('zoomed')
    ventana_info.resizable(width=False, height=False)

    fondo_info = cargarImagen("fondoin.png")
    label_fondo_info = Label(ventana_info, image=fondo_info)
    label_fondo_info.image = fondo_info
    label_fondo_info.place(relx=0.5, rely=0.5, anchor='center')

    foto1 = Image.open(os.path.join("imagenes", "foto1.png"))
    foto2 = Image.open(os.path.join("imagenes", "foto2.png"))

    max_size = (500, 500)
    foto1.thumbnail(max_size)
    foto2.thumbnail(max_size)

    carga_foto1 = ImageTk.PhotoImage(foto1)
    carga_foto2 = ImageTk.PhotoImage(foto2)

    labeliz = Label(ventana_info, image=carga_foto1)
    labeliz.image = carga_foto1
    labeliz.place(relx=0.25, rely=0.3, anchor='center')

    labelde = Label(ventana_info, image=carga_foto2)
    labelde.image = carga_foto2
    labelde.place(relx=0.75, rely=0.3, anchor='center')

    texto1 = Label(ventana_info, text="Nombre: Jeury Calel Vargas Vega\nIdentificación: 119750909", font=("Futura Bold Condensed BT", 24), bg="#ffffff")
    texto1.place(relx=0.25, rely=0.6, anchor='center')
    
    texto2 = tk.Label(ventana_info, text="Nombre: Elí Navarro Monge\nIdentificación: 305570203", font=("Futura Bold Condensed BT", 24), bg="#ffffff")
    texto2.place(relx=0.75, rely=0.6, anchor='center')
    
    texto3 = tk.Label(ventana_info, text="Fundamentos de Sistemas Computacionales\nIngeniería en Computadores (CE)\n2024\nLuis Alberto Chavarría Zamora\nCostaRica\n1.0", font=("Futura Bold Condensed BT", 24), bg="#ffffff")  # Fondo blanco para el texto
    texto3.place(relx=0.5, rely=0.8, anchor='center')

    cierrainfo = Button(ventana_info, text="X", bg="red", fg="black", command=lambda: [ventana_info.destroy(), ventana.deiconify()])
    cierrainfo.pack(pady=50)
    cierrainfo.place(relx=0.95, rely=0.09, anchor='center')
    cierrainfo.config(height=2, width=7)
    cierrainfo['font'] = fuente

VentanaInicio()
