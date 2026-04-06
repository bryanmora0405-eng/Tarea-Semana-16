from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = []
        self.contador_id = 1

    def agregar_tarea(self, descripcion):
        if descripcion.strip():
            nueva_tarea = Tarea(self.contador_id, descripcion)
            self.tareas.append(nueva_tarea)
            self.contador_id += 1
            return nueva_tarea
        return None

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
            return True
        return False

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            return True
        return False

    def obtener_todas(self):
        return self.tareas