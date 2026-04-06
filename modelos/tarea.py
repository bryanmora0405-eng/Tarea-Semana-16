class Tarea:
    def __init__(self, id_tarea, descripcion):
        self.id = id_tarea
        self.descripcion = descripcion
        self.completada = False

    def __str__(self):
        estado = "[Hecho]" if self.completada else "[Pendiente]"
        return f"{self.descripcion} {estado}"