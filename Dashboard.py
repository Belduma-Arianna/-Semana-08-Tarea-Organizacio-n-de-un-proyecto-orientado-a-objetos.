# Tarea de Programacion Orientada a Objetos
# Estudiante: ARIANNA ELIZABETH BELDUMA NAGUA
# Universidad Estatal Amazonica
import os
import subprocess

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    # Se han actualizado los nombres para que coincidan con tus carpetas UNIDAD 1 y UNIDAD 2
    unidades = {
        '1': 'UNIDAD 1',
        '2': 'UNIDAD 2'
    }

    while True:
        print("\n" + "═" * 40)
        print("   SISTEMA DE GESTIÓN PERSONAL - POO   ")
        print("   Estudiante: ARIANNA BELDUMA         ")
        print("═" * 40)
        
        for key in unidades:
            print(f"  [{key}] > {unidades[key]}")
        print("  [0] > Salir")

        eleccion_unidad = input("\nElige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    try:
        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
    except FileNotFoundError:
        print(f"\n[!] Error: No se encontró la carpeta física '{os.path.basename(ruta_unidad)}'.")
        print("Asegúrate de que la carpeta esté en la misma ubicación que este script.")
        return

    while True:
        print(f"\nSubmenú - {os.path.basename(ruta_unidad)}")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                indice = int(eleccion_carpeta) - 1
                if 0 <= indice < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

def mostrar_scripts(ruta_sub_carpeta):
    try:
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]
    except FileNotFoundError:
        return

    while True:
        print(f"\nScripts en {os.path.basename(ruta_sub_carpeta)}")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")
        print("9 - Menú Principal")

        eleccion = input("Selección: ")
        if eleccion == '0': break
        elif eleccion == '9': return
        else:
            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                    if mostrar_codigo(ruta_script):
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        input("\nPresiona Enter para continuar.")
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Entrada no válida.")

if __name__ == "__main__":
    mostrar_menu()

# --- NOTAS DE LA ESTUDIANTE: ARIANNA BELDUMA ---
# 1. Se personalizó la interfaz visual del menú principal agregando bordes decorativos.
# 2. Se incluyó el nombre de la estudiante en el encabezado del Dashboard.
# 3. Se modificaron los nombres de las carpetas a UNIDAD 1 y UNIDAD 2 para sincronizar con el repositorio.
# 4. Se agregaron comentarios descriptivos para facilitar la lectura del código.