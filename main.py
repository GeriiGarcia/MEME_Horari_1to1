import tkinter as tk
from tkinter import ttk
from form import create_form_frame
from data_page import create_data_frame

# Función para cambiar a la pantalla del formulario
def show_form():
    main_frame.pack_forget()
    data_frame.pack_forget()
    form_frame.pack(fill='both', expand=True)

# Función para volver al menú principal
def back_to_main():
    form_frame.pack_forget()
    data_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)

# Función para mostrar la página de datos
def show_data_page(hora='', tiempo_entrevista='', tiempo_cambio=''):
    form_frame.pack_forget()
    main_frame.pack_forget()
    for widget in data_frame.winfo_children():
        widget.destroy()
    create_data_frame(data_frame, back_to_main, hora, tiempo_entrevista, tiempo_cambio)
    data_frame.pack(fill='both', expand=True)

# Crear la ventana principal
root = tk.Tk()
root.title("1to1 APP")
root.geometry("600x500")

# Crear el menú principal
menubar = tk.Menu(root)
root.config(menu=menubar)

# Crear un menú de opciones
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Nuevo Horario", command=show_form)
file_menu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=file_menu)

# Crear otro menú de opciones (desplegable)
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Opción 1")
edit_menu.add_command(label="Opción 2")
menubar.add_cascade(label="Editar", menu=edit_menu)

# Frame del menú principal
main_frame = ttk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Crear el frame del formulario llamando a una función del archivo form.py
form_frame = create_form_frame(root, back_to_main, show_data_page)

# Crear el frame de la página de datos
data_frame = ttk.Frame(root)

# Contenido del menú principal
main_label = ttk.Label(main_frame, text="Menú Principal", font=("Helvetica", 16))
main_label.pack(pady=20)

nuevo_horario_button = ttk.Button(main_frame, text="Nuevo Horario", command=show_form)
nuevo_horario_button.pack(pady=10)

dummy_button = ttk.Button(main_frame, text="Botón sin acción")
dummy_button.pack(pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()