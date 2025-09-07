from mascota import Mascota

class ControlMascota:
    def __init__(self):
        self.mascotas = []

    def listar(self):
        return self.mascotas
    
    def agregar(self, nombre, tipo):
        nuevo = Mascota(len(self.mascotas)+1, nombre, tipo)
        self.mascotas.append(nuevo)
        return nuevo
    
    def obtener_por_id(self, id):
        return next((m for m in self.mascotas if m.id == id), None)
    
    def eliminar(self, id):
        mascota = self.obtener_por_id(id)
        if mascota:
            self.mascotas.remove(mascota)
            return True
        return False
    
    def modificar(self, id, nombre=None, tipo=None):
        mascota = self.obtener_por_id(id)
        if mascota:
            if nombre:
                mascota.nombre = nombre
            if tipo:
                mascota.tipo = tipo
            return mascota
        return None