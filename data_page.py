import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

hora_general = "15:00"
tiempo_entrevista_general = "5"
tiempo_cambio_general = "1"

def create_data_frame(data_frame, back_to_main, hora='', tiempo_entrevista='', tiempo_cambio='', empresas=[], num_empresas=0, alumnos={}, add_empresa=None, add_alumno=None):
    # Contenido de la página de datos
    data_label = ttk.Label(data_frame, text="Datos Introducidos", font=("Helvetica", 16))
    data_label.pack(pady=20)

    hora_label = ttk.Label(data_frame, text=f"Hora: {hora_general}")
    hora_label.pack(side='top', padx=10)

    tiempo_entrevista_label = ttk.Label(data_frame, text=f"Tiempo de Entrevista: {tiempo_entrevista_general} minutos")
    tiempo_entrevista_label.pack(side='top', padx=10)

    tiempo_cambio_label = ttk.Label(data_frame, text=f"Tiempo de Cambio: {tiempo_cambio_general} minutos")
    tiempo_cambio_label.pack(side='top', padx=10)

    # Crear tabla dinámica
    table_frame = ttk.Frame(data_frame)
    table_frame.pack(pady=20, fill='both', expand=True)

    try:
        start_time = datetime.strptime(hora_general, '%H:%M')
        interview_time = int(tiempo_entrevista_general)
        change_time = int(tiempo_cambio_general)

        tree = ttk.Treeview(table_frame)
        tree.pack(fill='both', expand=True)

        columns = ["Horas"] + empresas[:num_empresas]
        tree["columns"] = tuple(columns)
        tree.heading("#0", text="")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("Horas", text="Horas")
        tree.column("Horas", width=100, anchor='center')

        for empresa in empresas[:num_empresas]:
            tree.heading(empresa, text=empresa)
            tree.column(empresa, width=100, anchor='center')

        current_time = start_time
        for i in range(50):
            row_values = [current_time.strftime('%H:%M')]
            for empresa in empresas[:num_empresas]:
                if empresa in alumnos and len(alumnos[empresa]) > i:
                    row_values.append(alumnos[empresa][i])
                else:
                    row_values.append("")
            tree.insert("", tk.END, values=row_values)
            current_time += timedelta(minutes=interview_time + change_time)

        button_frame = ttk.Frame(data_frame)
        button_frame.pack(pady=10)

        add_empresa_button = ttk.Button(button_frame, text="Añadir Empresa", command=add_empresa)
        add_empresa_button.pack(side='left', padx=10)

        add_alumno_button = ttk.Button(button_frame, text="Añadir Alumno", command=add_alumno)
        add_alumno_button.pack(side='left', padx=10)

        back_button = ttk.Button(data_frame, text="Volver al Menú Principal", command=back_to_main)
        back_button.pack(pady=20)

    except ValueError:
        ttk.Label(data_frame, text="Error: Verifica los valores de hora, tiempo de entrevista y tiempo de cambio.", foreground='red').pack(pady=20)
