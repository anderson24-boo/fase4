from entidades_base import EntidadBase
from excepciones import ErrorDescuentoInvalido

class Servicio(EntidadBase):
    def __init__(self, nombre, descripcion, precio_base):
        super().__init__(None, nombre)
        self._descripcion = descripcion
        self._precio_base = precio_base

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def precio_base(self):
        return self._precio_base

    def calcular_costo(self, descuento=0, impuestos=0):
        if descuento < 0 or descuento > 100:
            raise ErrorDescuentoInvalido()
        subtotal = self._precio_base * (1 - descuento / 100)
        total = subtotal * (1 + impuestos)
        return total

    def obtener_informacion(self):
        return f"Servicio: {self.nombre} | {self.descripcion} | Precio base: ${self.precio_base:,}"