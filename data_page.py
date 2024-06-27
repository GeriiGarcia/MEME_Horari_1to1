import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime, timedelta
import openpyxl
from openpyxl import Workbook
from Levenshtein import distance as levenshtein_distance

def create_data_frame(data_frame, back_to_main, hora='', tiempo_entrevista='', tiempo_cambio='', empresas=[], num_empresas=0, alumnos={}, add_empresa=None, add_alumno=None):
    # Contenido de la página de datos
    data_label = ttk.Label(data_frame, text="Datos Introducidos", font=("Helvetica", 16))
    data_label.pack(pady=20)

    hora_label = ttk.Label(data_frame, text=f"Hora: {hora}")
    hora_label.pack(side='top', padx=10)

    tiempo_entrevista_label = ttk.Label(data_frame, text=f"Tiempo de Entrevista: {tiempo_entrevista} minutos")
    tiempo_entrevista_label.pack(side='top', padx=10)

    tiempo_cambio_label = ttk.Label(data_frame, text=f"Tiempo de Cambio: {tiempo_cambio} minutos")
    tiempo_cambio_label.pack(side='top', padx=10)

    # Crear tabla dinámica
    table_frame = ttk.Frame(data_frame)
    table_frame.pack(pady=20, fill='both', expand=True)

    try:
        start_time = datetime.strptime(hora, '%H:%M')
        interview_time = int(tiempo_entrevista)
        change_time = int(tiempo_cambio)

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

        def export_to_xlsx():
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
            if file_path:
                wb = Workbook()
                ws = wb.active
                ws.append(columns)
                for row_id in tree.get_children():
                    row = tree.item(row_id)['values']
                    ws.append(row)
                wb.save(file_path)

        def colorear_similares():
            # Recorrer el diccionario de alumnos y las empresas para encontrar similares
            tags_dict = {}

            for empresa in empresas[:num_empresas]:
                if empresa in alumnos:
                    for i, alumno_i in enumerate(alumnos[empresa]):
                        for empresa2 in empresas[:num_empresas]:
                            if empresa2 in alumnos:
                                for j, alumno_j in enumerate(alumnos[empresa2]):
                                    if (empresa != empresa2 or i != j) and alumno_i != "" and alumno_j != "":
                                        dist = levenshtein_distance(alumno_i, alumno_j)
                                        if dist == 1 or dist ==2:
                                            print(f"Empresa: {empresa} - Alumno: {alumno_i} en la fila {i + 1} con distancia {dist}")
                                            print(f"Empresa: {empresa2} - Alumno: {alumno_j} en la fila {j + 1} con distancia {dist}")
                                            print(" ")

            
            
            data = []
            for row_id in tree.get_children():
                row = tree.item(row_id)['values']
                data.append(row)

            # Crear una nueva ventana para mostrar las celdas similares
            new_window = tk.Toplevel(data_frame)
            new_window.title("Celdas Similares")

            # Crear un Canvas y un Frame dentro del Canvas para permitir el desplazamiento
            canvas = tk.Canvas(new_window)
            scroll_y = tk.Scrollbar(new_window, orient="vertical", command=canvas.yview)
            scroll_x = tk.Scrollbar(new_window, orient="horizontal", command=canvas.xview)

            scrollable_frame = ttk.Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

            canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

            # Añadir los encabezados de las empresas
            for j, empresa in enumerate(empresas[:num_empresas], start=1):
                label = tk.Label(scrollable_frame, text=empresa, borderwidth=1, relief="solid", padx=5, pady=5)
                label.grid(row=0, column=j, padx=5, pady=5)

            # Crear etiquetas en el frame desplazable
            labels = []
            for i, row in enumerate(data):
                row_labels = []
                for j, cell in enumerate(row):
                    label = tk.Label(scrollable_frame, text=cell, borderwidth=1, relief="solid", padx=5, pady=5)
                    label.grid(row=i+1, column=j, padx=5, pady=5)
                    row_labels.append(label)
                labels.append(row_labels)

            # Encontrar y colorear las celdas similares
            for i, row in enumerate(data):
                for j, cell in enumerate(row):
                    if j == 0:  # Ignorar la columna de horas
                        continue
                    for ii, row2 in enumerate(data):
                        for jj, cell2 in enumerate(row2):
                            if jj == 0:  # Ignorar la columna de horas
                                continue
                            if (i != ii or j != jj) and cell and cell2 and (levenshtein_distance(cell, cell2) == 1 or levenshtein_distance(cell, cell2) == 2):
                                labels[i][j].config(bg='yellow')
                                labels[ii][jj].config(bg='yellow')

            canvas.pack(side="left", fill="both", expand=True)
            scroll_y.pack(side="right", fill="y")
            scroll_x.pack(side="bottom", fill="x")





            for empresa in empresas[:num_empresas]:
                if empresa in alumnos:
                    for i, alumno_i in enumerate(alumnos[empresa]):
                        for empresa2 in empresas[:num_empresas]:
                            if empresa2 in alumnos:
                                for j, alumno_j in enumerate(alumnos[empresa2]):
                                    if (empresa != empresa2 or i != j) and alumno_i != "" and alumno_j != "":
                                        dist = levenshtein_distance(alumno_i, alumno_j)
                                        if dist == 1 or dist == 2:
                                            tag_name = f"similar_{empresa}_{i}_{empresa2}_{j}"
                                            if (empresa, i) not in tags_dict:
                                                tags_dict[(empresa, i)] = []
                                            if (empresa2, j) not in tags_dict:
                                                tags_dict[(empresa2, j)] = []
                                            tags_dict[(empresa, i)].append(tag_name)
                                            tags_dict[(empresa2, j)].append(tag_name)

            for (empresa, index), tags in tags_dict.items():
                for row_id in tree.get_children():
                    row = tree.item(row_id)['values']
                    col_index = columns.index(empresa)
                    if len(row) > col_index and row[col_index] == alumnos[empresa][index]:
                        for tag_name in tags:
                            current_tags = tree.item(row_id, 'tags')
                            if isinstance(current_tags, str):
                                current_tags = (current_tags,)
                            elif current_tags is None:
                                current_tags = ()
                            new_tags = current_tags + (tag_name,)
                            tree.item(row_id, tags=new_tags)
                            tree.tag_configure(tag_name, background="yellow")


        button_frame = ttk.Frame(data_frame)
        button_frame.pack(pady=10)

        add_empresa_button = ttk.Button(button_frame, text="Añadir Empresa", command=add_empresa)
        add_empresa_button.pack(side='left', padx=10)

        add_alumno_button = ttk.Button(button_frame, text="Añadir Alumno", command=add_alumno)
        add_alumno_button.pack(side='left', padx=10)

        export_xlsx_button = ttk.Button(button_frame, text="Exportar a XLSX", command=export_to_xlsx)
        export_xlsx_button.pack(side='left', padx=10)

        color_similares_button = ttk.Button(button_frame, text="Colorear Similares", command=colorear_similares)
        color_similares_button.pack(side='left', padx=10)

        back_button = ttk.Button(data_frame, text="Volver al Menú Principal", command=back_to_main)
        back_button.pack(pady=20)

    except ValueError:
        ttk.Label(data_frame, text="Error: Verifica los valores de hora, tiempo de entrevista y tiempo de cambio.", foreground='red').pack(pady=20)