import tkinter as tk
from tkinter import messagebox

class TareaApp:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Gestor de Tareas v2 - Atajos de Teclado")
        self.root.geometry("400x450")

        # --- Interfaz Gráfica ---
        tk.Label(root, text="Nueva Tarea (Enter para añadir):", font=('Arial', 10, 'bold')).pack(pady=5)
        self.entry_tarea = tk.Entry(root, width=40)
        self.entry_tarea.pack(pady=5)
        self.entry_tarea.focus_set() # Pone el cursor aquí al iniciar

        self.btn_añadir = tk.Button(root, text="Añadir Tarea", command=self.añadir_tarea, bg="#4CAF50", fg="white")
        self.btn_añadir.pack(pady=5)

        tk.Label(root, text="Atajos: [C] Completar | [Del/D] Eliminar | [Esc] Salir", font=('Arial', 8, 'italic')).pack()
        
        self.lista_box = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.lista_box.pack(pady=10, padx=10)

        # --- REGISTRO DE ATAJOS DE TECLADO ---
        
        # 1. Enter para añadir (este se queda igual porque es tecla especial)
        self.entry_tarea.bind('<Return>', lambda e: self.añadir_tarea())
        
        # 2. Tecla 'c' para completar (sin los < >)
        self.root.bind('c', lambda e: self.marcar_completada())
        self.root.bind('C', lambda e: self.marcar_completada())
        
        # 3. Tecla 'd' o 'Delete' para eliminar
        self.root.bind('d', lambda e: self.eliminar_tarea())
        self.root.bind('D', lambda e: self.eliminar_tarea())
        self.root.bind('<Delete>', lambda e: self.eliminar_tarea()) # Este sí lleva < >
        
        # 4. Escape para cerrar
        self.root.bind('<Escape>', lambda e: self.root.destroy())

    def actualizar_lista(self):
        self.lista_box.delete(0, tk.END)
        for tarea in self.servicio.obtener_todas():
            texto = str(tarea)
            self.lista_box.insert(tk.END, texto)
            if tarea.completada:
                self.lista_box.itemconfig(tk.END, fg="gray")

    def añadir_tarea(self):
        desc = self.entry_tarea.get()
        if self.servicio.agregar_tarea(desc):
            self.actualizar_lista()
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "Escribe una descripción")

    def marcar_completada(self):
        seleccion = self.lista_box.curselection()
        if seleccion:
            self.servicio.marcar_completada(seleccion[0])
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista_box.curselection()
        if seleccion:
            self.servicio.eliminar_tarea(seleccion[0])
            self.actualizar_lista()