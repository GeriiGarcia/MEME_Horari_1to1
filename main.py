import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from form import create_form_frame
from data_page import create_data_frame

# Variables globales para almacenar empresas y alumnos
empresas = []
num_empresas = 0
alumnos = {}

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
    create_data_frame(data_frame, back_to_main, hora, tiempo_entrevista, tiempo_cambio, empresas, num_empresas, alumnos, add_empresa, add_alumno)
    data_frame.pack(fill='both', expand=True)

# Función para añadir una empresa
def add_empresa():
    global num_empresas
    def save_empresa():
        global num_empresas
        nombre_empresa = empresa_entry.get()
        if nombre_empresa and num_empresas < 50:  # Limitar a 50 empresas
            empresas.append(nombre_empresa)
            alumnos[nombre_empresa] = []
            num_empresas += 1
            empresa_window.destroy()
            show_data_page()

    empresa_window = tk.Toplevel(root)
    empresa_window.title("Añadir Empresa")
    ttk.Label(empresa_window, text="Nombre de la Empresa:").pack(pady=10)
    empresa_entry = ttk.Entry(empresa_window)
    empresa_entry.pack(pady=5)
    ttk.Button(empresa_window, text="Guardar", command=save_empresa).pack(pady=10)

# Función para añadir un alumno
def add_alumno():
    def save_alumno():
        nombre_alumno = alumno_entry.get()
        nombre_empresa = empresa_combobox.get()
        if nombre_alumno.lower() == "hola":  # Verificar si el nombre es "hola"
            messagebox.showerror("Error", "El nombre del alumno no puede ser 'hola'.")
        elif nombre_alumno and nombre_empresa in empresas:
            alumnos[nombre_empresa].append(nombre_alumno)
            alumno_window.destroy()
            show_data_page()

    alumno_window = tk.Toplevel(root)
    alumno_window.title("Añadir Alumno")
    ttk.Label(alumno_window, text="Nombre del Alumno:").pack(pady=10)
    alumno_entry = ttk.Entry(alumno_window)
    alumno_entry.pack(pady=5)
    ttk.Label(alumno_window, text="Nombre de la Empresa:").pack(pady=10)
    empresa_combobox = ttk.Combobox(alumno_window, values=empresas[:num_empresas])
    empresa_combobox.pack(pady=5)
    ttk.Button(alumno_window, text="Guardar", command=save_alumno).pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("1to1 APP")
root.geometry("800x600")

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
edit_menu.add_command(label="Añadir Empresa", command=add_empresa)
edit_menu.add_command(label="Añadir Alumno", command=add_alumno)
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
