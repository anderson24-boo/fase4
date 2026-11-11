from gestor_logs import GestorLogs
from cliente import Cliente

def main():
    # Limpiamos el registro al iniciar
    GestorLogs.limpiar()
    GestorLogs.registrar("Sistema iniciado correctamente", "INFO")

    # Creamos un cliente de ejemplo
    cliente1 = Cliente("Juan Pérez", "123456789", "juan@correo.com", "3001234567")
    print(cliente1.obtener_informacion())
    
    GestorLogs.registrar(f"Cliente creado: {cliente1.nombre}", "INFO")
    GestorLogs.registrar("Sistema finalizado", "INFO")
    print("✅ Todo funcionó correctamente")

if __name__ == "__main__":
    main()