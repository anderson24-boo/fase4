class ErrorSistemaReservas(Exception):
    """Excepción base personalizada del sistema"""
    def __init__(self, mensaje="Error en el sistema de reservas"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorClienteInvalido(ErrorSistemaReservas):
    """Se lanza cuando los datos del cliente no son válidos"""
    def __init__(self, mensaje="Los datos del cliente no son válidos"):
        super().__init__(mensaje)

class ErrorServicioInvalido(ErrorSistemaReservas):
    """Se lanza cuando el servicio no es válido"""
    def __init__(self, mensaje="El servicio seleccionado no es válido"):
        super().__init__(mensaje)

class ErrorReservaInvalida(ErrorSistemaReservas):
    """Se lanza cuando hay un problema con la reserva"""
    def __init__(self, mensaje="La reserva no es válida"):
        super().__init__(mensaje)

class ErrorFechaInvalida(ErrorSistemaReservas):
    """Se lanza cuando la fecha de reserva no es correcta"""
    def __init__(self, mensaje="La fecha seleccionada no es válida"):
        super().__init__(mensaje)

class ErrorDescuentoInvalido(ErrorSistemaReservas):
    """Se lanza cuando el descuento está fuera de rango"""
    def __init__(self, mensaje="El descuento debe estar entre 0 y 100"):
        super().__init__(mensaje)