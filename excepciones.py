class ErrorSistemaReservas(Exception):
    """Clase base para todas las excepciones del sistema"""
    def __init__(self, mensaje="Error en el sistema de reservas"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ErrorCorreoInvalido(ErrorSistemaReservas):
    """Se lanza cuando el formato del correo no es válido"""
    def __init__(self, mensaje="El formato del correo no es válido"):
        super().__init__(mensaje)


class ErrorDescuentoInvalido(ErrorSistemaReservas):
    """Se lanza cuando el descuento está fuera del rango permitido"""
    def __init__(self, mensaje="El descuento debe estar entre 0 y 100"):
        super().__init__(mensaje)


class ErrorReservaInvalida(ErrorSistemaReservas):
    """Se lanza cuando hay datos incompletos o incorrectos en la reserva"""
    def __init__(self, mensaje="Faltan datos del cliente o del servicio"):
        super().__init__(mensaje)


class ErrorServicioInvalido(ErrorSistemaReservas):
    """Se lanza cuando se intenta usar un servicio no disponible"""
    def __init__(self, mensaje="El servicio seleccionado no está disponible"):
        super().__init__(mensaje)


class ErrorFechaInvalida(ErrorSistemaReservas):
    """Se lanza cuando la fecha de reserva no es correcta"""
    def __init__(self, mensaje="La fecha de la reserva debe ser posterior a hoy"):
        super().__init__(mensaje)