import tkinter as tk
from tkinter import ttk

def create_data_frame(data_frame, back_to_main, hora='', tiempo_entrevista='', tiempo_cambio=''):
    # Contenido de la página de datos
    data_label = ttk.Label(data_frame, text="Datos Introducidos", font=("Helvetica", 16))
    data_label.pack(pady=20)

    hora_label = ttk.Label(data_frame, text=f"Hora: {hora}")
    hora_label.pack(pady=5)

    tiempo_entrevista_label = ttk.Label(data_frame, text=f"Tiempo de Entrevista: {tiempo_entrevista}")
    tiempo_entrevista_label.pack(pady=5)

    tiempo_cambio_label = ttk.Label(data_frame, text=f"Tiempo de Cambio: {tiempo_cambio}")
    tiempo_cambio_label.pack(pady=5)

    back_button = ttk.Button(data_frame, text="Volver al Menú Principal", command=back_to_main)
    back_button.pack(pady=20)

    return data_frame
