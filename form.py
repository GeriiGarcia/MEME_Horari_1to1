import tkinter as tk
from tkinter import ttk

def create_form_frame(root, back_command, show_data_page):
    # Frame del formulario
    form_frame = ttk.Frame(root)

    # Contenido del formulario
    form_label = ttk.Label(form_frame, text="Formulario de Nuevo Horario", font=("Helvetica", 16))
    form_label.pack(pady=20)

    hora_label = ttk.Label(form_frame, text="Hora:")
    hora_label.pack(pady=5)
    hora_entry = ttk.Entry(form_frame)
    hora_entry.pack(pady=5)

    tiempo_entrevista_label = ttk.Label(form_frame, text="Tiempo de Entrevista:")
    tiempo_entrevista_label.pack(pady=5)
    tiempo_entrevista_entry = ttk.Entry(form_frame)
    tiempo_entrevista_entry.pack(pady=5)

    tiempo_cambio_label = ttk.Label(form_frame, text="Tiempo de Cambio:")
    tiempo_cambio_label.pack(pady=5)
    tiempo_cambio_entry = ttk.Entry(form_frame)
    tiempo_cambio_entry.pack(pady=5)

    def confirm_action():
        hora = hora_entry.get()
        tiempo_entrevista = tiempo_entrevista_entry.get()
        tiempo_cambio = tiempo_cambio_entry.get()
        show_data_page(hora, tiempo_entrevista, tiempo_cambio)

    confirm_button = ttk.Button(form_frame, text="Confirmar", command=confirm_action)
    confirm_button.pack(pady=10)

    back_button = ttk.Button(form_frame, text="Volver al Menú Principal", command=back_command)
    back_button.pack(pady=20)

    return form_frame
