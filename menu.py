import subprocess
import sys

# Opciones del menú con las rutas de los archivos de prueba en cada carpeta
PRUEBAS = {
    "1": ("Prueba de Caída Libre", "Taller 1/caida_libre/pruebas.py"),
    "2": ("Prueba de Cálculo de Desplazamiento", "Taller 1/calculo_desplazamiento/pruebas.py"),
    "3": ("Prueba de Conversor de Velocidad", "Taller 1/conversor_velocidad/pruebas.py"),
    "4": ("Prueba de Lanzamiento de Proyectiles", "Taller 1/lanzamiento_proyectiles/pruebas.py"),
    "5": ("Prueba de Producto Escalar", "Taller 1/producto_escalar/pruebas.py"),
    "6": ("Prueba de Suma de Vectores", "Taller 1/suma_vectores/pruebas.py"),
    "0": ("Salir", None),
}

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=== Taller 1: Ejecutar Pruebas ===")
    for key, (nombre, _) in PRUEBAS.items():
        print(f"{key}. {nombre}")

def ejecutar_prueba(opcion):
    """Ejecuta el archivo pruebas.py de la opción seleccionada."""
    if opcion in PRUEBAS:
        nombre, ruta = PRUEBAS[opcion]
        if ruta:
            print(f"\nEjecutando {nombre}...\n")
            subprocess.run([sys.executable, ruta])  # Ejecuta el archivo pruebas.py de la carpeta correspondiente
        else:
            print("\nSaliendo del sistema. ¡Hasta luego!")
            sys.exit(0)
    else:
        print("\n❌ Opción no válida. Intenta de nuevo.")

def main():
    """Bucle principal del menú."""
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ").strip()
        ejecutar_prueba(opcion)

if __name__ == "__main__":
    main()
