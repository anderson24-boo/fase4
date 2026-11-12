from entidades_base import EntidadBase
from cliente import Cliente
from servicio import Servicio
from datetime import datetime

class Reserva(EntidadBase):
    def __init__(self, id, cliente, servicio, fecha, duracion_horas):
        super().__init__(id, f"Reserva-{id}")
        if not isinstance(cliente, Cliente):
            raise ValueError("El cliente no es válido")
        if not isinstance(servicio, Servicio):
            raise ValueError("El servicio no es válido")
        self._cliente = cliente
        self._servicio = servicio
        self._fecha = fecha
        self._duracion_horas = duracion_horas
        self._costo_total = 0.0

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def fecha(self):
        return self._fecha

    @property
    def duracion_horas(self):
        return self._duracion_horas

    @property
    def costo_total(self):
        return self._costo_total

    def calcular_total(self):
        self._costo_total = self._servicio.calcular_costo() * self._duracion_horas
        return self._costo_total

    def obtener_informacion(self):
        return f"Reserva: {self.nombre}\n  Cliente: {self.cliente.nombre}\n  Servicio: {self.servicio.nombre}\n  Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}\n  Duración: {self.duracion_horas} horas\n  Costo total: ${self.calcular_total():,}"