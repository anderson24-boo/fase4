from abc import ABC, abstractmethod

class EntidadBase(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def obtener_informacion(self):
        pass

    def __str__(self):
        return self.nombre