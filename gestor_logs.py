from datetime import datetime
import os

class GestorLogs:
    ARCHIVO = "registro_eventos.txt"

    @staticmethod
    def registrar(mensaje, tipo="INFO"):
        try:
            fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            linea = f"[{fecha}] [{tipo}] {mensaje}\n"
            with open(GestorLogs.ARCHIVO, "a", encoding="utf-8") as f:
                f.write(linea)
        except Exception as e:
            print("No se pudo guardar el registro:", e)

    @staticmethod
    def limpiar():
        if os.path.exists(GestorLogs.ARCHIVO):
            os.remove(GestorLogs.ARCHIVO)
            GestorLogs.registrar("Inicio del sistema", "INFO")
            