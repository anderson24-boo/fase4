from entidades_base import EntidadBase
from excepciones import ErrorCorreoInvalido
import re

class Cliente(EntidadBase):
    def __init__(self, nombre, identificacion, correo, telefono):
        super().__init__(None, nombre)
        self._identificacion = identificacion
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            raise ErrorCorreoInvalido()
        self._correo = correo
        self._telefono = telefono

    @property
    def identificacion(self):
        return self._identificacion

    @property
    def correo(self):
        return self._correo

    @property
    def telefono(self):
        return self._telefono

    def obtener_informacion(self):
        return f"Cliente: {self.nombre} | ID: {self.identificacion} | Correo: {self.correo} | Teléfono: {self.telefono}"