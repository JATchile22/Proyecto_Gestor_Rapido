import os
import sys
from datetime import datetime

VERSION = "1.0.0"
APP_NAME = "GestorRapido"


def obtener_ruta_notas() -> str:
    """Guarda las notas en una carpeta segura del usuario actual."""
    base_dir = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~/.local/share")
    carpeta_app = os.path.join(base_dir, APP_NAME)
    os.makedirs(carpeta_app, exist_ok=True)
    return os.path.join(carpeta_app, "notas.txt")

def funcion_1_convertir_unidades() -> None:
    """Función principal 1: convierte kilogramos a libras y kilómetros a millas."""
    print("\n--- 1. Conversor de Unidades (kg <-> lb | km <-> mi) ---")
    try:
        valor = float(input("Ingresa un número positivo: ").strip().replace(",", "."))
        if valor < 0:
            print("Error: ingresa un valor mayor o igual a 0.")
            return
        print("a) Kilogramos a Libras")
        print("b) Kilómetros a Millas")
        opcion = input("Elige (a/b): ").strip().lower()
        if opcion == "a":
            resultado = valor * 2.20462
            print(f"Resultado: {valor:.2f} kg = {resultado:.2f} lb")
        elif opcion == "b":
            resultado = valor * 0.621371
            print(f"Resultado: {valor:.2f} km = {resultado:.2f} mi")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Error: debes ingresar un número válido.")


def funcion_2_agregar_nota() -> None:
    """Función principal 2: guarda una nota con fecha y hora."""
    print("\n--- 2. Agregar Nota ---")
    texto = input("Escribe tu nota: ").strip()
    if not texto:
        print("La nota está vacía; no se guardó nada.")
        return
    ruta = obtener_ruta_notas()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    linea = f"[{fecha}] {texto}\n"
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(linea)
    print(f"Nota guardada correctamente en: {ruta}")


def funcion_3_listar_notas() -> None:
    """Función principal 3: muestra todas las notas guardadas."""
    print("\n--- 3. Ver Notas Guardadas ---")
    ruta = obtener_ruta_notas()
    if not os.path.exists(ruta):
        print("Aún no hay notas registradas.")
        return
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read().strip()
    if not contenido:
        print("El archivo de notas está vacío.")
        return
    print(contenido)


def mostrar_menu() -> None:
    print(f"\n=== {APP_NAME} v{VERSION} ===")
    print("1. Convertir unidades (kg/lb, km/mi)")
    print("2. Agregar nota")
    print("3. Ver notas guardadas")
    print("4. Salir")


def main() -> None:
    if "--version" in sys.argv or "-v" in sys.argv:
        print(f"{APP_NAME} {VERSION}")
        return

    while True:
        mostrar_menu()
        eleccion = input("Selecciona una opción (1-4): ").strip()
        if eleccion == "1":
            funcion_1_convertir_unidades()
        elif eleccion == "2":
            funcion_2_agregar_nota()
        elif eleccion == "3":
            funcion_3_listar_notas()
        elif eleccion == "4":
            print("Saliendo de GestorRapido...")
            break
        else:
            print("Opción no válida. Intenta con 1, 2, 3 o 4.")


if __name__ == "__main__":
    main()
