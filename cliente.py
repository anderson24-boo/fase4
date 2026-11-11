from entidades_base import EntidadBase

class Cliente(EntidadBase):
    def __init__(self, nombre, identificacion, correo, telefono):
        super().__init__(nombre)
        self.identificacion = identificacion
        self.correo = correo
        self.telefono = telefono

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, ID: {self.identificacion}, Correo: {self.correo}, Teléfono: {self.telefono}"