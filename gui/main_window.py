import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from logic.file_loader import read_file
from db.database import insert_data, get_all_data

def run_gui():
    window = tk.Tk()
    window.title("NotiPrecio - Sistema de Gestión de Productos")
    window.geometry("800x600")
    
    # Frame principal que contendrá las diferentes vistas
    main_frame = tk.Frame(window)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    def show_main_menu():
        """Muestra el menú principal con las 3 opciones"""
        # Limpiar el frame principal
        for widget in main_frame.winfo_children():
            widget.destroy()
        
        # Título
        title_label = tk.Label(
            main_frame, 
            text="NotiPrecio - Sistema de Gestión de Productos",
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=30)
        
        # Subtítulo
        subtitle_label = tk.Label(
            main_frame,
            text="Seleccione una opción:",
            font=("Arial", 12)
        )
        subtitle_label.pack(pady=10)
        
        # Botón 1: Subir archivos
        btn_upload = tk.Button(
            main_frame,
            text="Subir archivos",
            font=("Arial", 14),
            width=25,
            height=2,
            command=show_upload_window,
            bg="#4CAF50",
            fg="white",
            cursor="hand2"
        )
        btn_upload.pack(pady=15)
        
        # Botón 2: Visualizar datos
        btn_view = tk.Button(
            main_frame,
            text="Visualizar los datos",
            font=("Arial", 14),
            width=25,
            height=2,
            command=show_data_viewer,
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        )
        btn_view.pack(pady=15)
        
        # Botón 3: Salir
        btn_exit = tk.Button(
            main_frame,
            text="Salir",
            font=("Arial", 14),
            width=25,
            height=2,
            command=window.quit,
            bg="#f44336",
            fg="white",
            cursor="hand2"
        )
        btn_exit.pack(pady=15)
    
    def show_upload_window():
        """Muestra la ventana para subir archivos"""
        # Limpiar el frame principal
        for widget in main_frame.winfo_children():
            widget.destroy()
        
        # Título
        title_label = tk.Label(
            main_frame,
            text="Subir archivos a la base de datos",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=20)
        
        # Instrucciones
        info_label = tk.Label(
            main_frame,
            text="Seleccione un archivo CSV o Excel para cargar los datos",
            font=("Arial", 11)
        )
        info_label.pack(pady=10)
        
        def load_and_insert():
            file_path = filedialog.askopenfilename(
                title="Seleccionar archivo CSV o Excel",
                filetypes=[("CSV", "*.csv"), ("Excel", "*.xls *.xlsx"), ("Todos los archivos", "*.*")]
            )
            if not file_path:
                return
            try:
                df = read_file(file_path)
                insert_data(df)
                messagebox.showinfo("Éxito", f"Datos cargados correctamente.\n{len(df)} registros insertados.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar los datos:\n{str(e)}")
        
        # Botón para seleccionar archivo
        btn_select = tk.Button(
            main_frame,
            text="Seleccionar archivo",
            font=("Arial", 12),
            width=20,
            height=2,
            command=load_and_insert,
            bg="#4CAF50",
            fg="white",
            cursor="hand2"
        )
        btn_select.pack(pady=30)
        
        # Botón para volver al menú principal
        btn_back = tk.Button(
            main_frame,
            text="Volver al menú principal",
            font=("Arial", 11),
            width=20,
            command=show_main_menu,
            bg="#757575",
            fg="white",
            cursor="hand2"
        )
        btn_back.pack(pady=10)
    
    def show_data_viewer():
        """Muestra la ventana para visualizar los datos de la base de datos"""
        # Limpiar el frame principal
        for widget in main_frame.winfo_children():
            widget.destroy()
        
        # Título
        title_label = tk.Label(
            main_frame,
            text="Visualizar datos de la base de datos",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=10)
        
        # Frame para la tabla con scrollbars
        table_frame = tk.Frame(main_frame)
        table_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Scrollbars
        scrollbar_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        scrollbar_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Treeview para mostrar los datos
        tree = ttk.Treeview(
            table_frame,
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set,
            show='headings'
        )
        scrollbar_y.config(command=tree.yview)
        scrollbar_x.config(command=tree.xview)
        
        def refresh_data():
            """Actualiza los datos en la tabla"""
            try:
                # Limpiar datos existentes
                for item in tree.get_children():
                    tree.delete(item)
                
                # Obtener datos de la base de datos
                columns, rows = get_all_data()
                
                # Configurar columnas
                tree['columns'] = columns
                for col in columns:
                    tree.heading(col, text=col.replace('_', ' ').title())
                    tree.column(col, width=120, anchor=tk.CENTER)
                
                # Insertar datos
                for row in rows:
                    tree.insert('', tk.END, values=row)
                
                # Ajustar ancho de columnas según contenido
                for col in columns:
                    tree.column(col, width=max(120, len(col) * 10))
                
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar los datos:\n{str(e)}")
        
        # Botón para actualizar datos
        btn_refresh = tk.Button(
            main_frame,
            text="Actualizar datos",
            font=("Arial", 11),
            width=15,
            command=refresh_data,
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        )
        btn_refresh.pack(pady=5)
        
        # Empaquetar el treeview
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Cargar datos iniciales
        refresh_data()
        
        # Botón para volver al menú principal
        btn_back = tk.Button(
            main_frame,
            text="Volver al menú principal",
            font=("Arial", 11),
            width=20,
            command=show_main_menu,
            bg="#757575",
            fg="white",
            cursor="hand2"
        )
        btn_back.pack(pady=10)
    
    # Mostrar el menú principal al iniciar
    show_main_menu()
    
    window.mainloop()
