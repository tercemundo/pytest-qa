# calculadora.py
import subprocess
import sys
import os

def sumar(a, b):
   """Suma dos números y devuelve el resultado."""
   return a + b

def restar(a, b):
   """Resta el segundo número del primero y devuelve el resultado."""
   return a - b

def ejecutar_tests():
    """Ejecuta los tests de pytest desde el script y muestra el resultado."""
    print("\n" + "="*30)
    print("  EJECUTANDO PRUEBAS CON PYTEST")
    print("="*30)

    # Forzar la codificación a UTF-8 para el subproceso es crucial en Windows
    # para manejar caracteres especiales como los emojis.
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"

    # Usamos sys.executable para asegurarnos de que se usa el pytest del entorno correcto.
    # El flag '-s' es para que se muestren los prints personalizados de los tests.
    # capture_output=True para capturar la salida y mostrarla. text=True para decodificarla.
    proceso = subprocess.run(
        [sys.executable, "-m", "pytest", "-s"],
        capture_output=True, text=True, encoding='utf-8',
        env=env
    )

    # Imprimimos la salida estándar de pytest (los resultados de los tests)
    print(proceso.stdout)
    if proceso.stderr:
        print(proceso.stderr)

    print("="*30)
    if proceso.returncode == 0:
        print("✅ ¡Todos los tests pasaron exitosamente!")
    else:
        print("❌ ¡Algunos tests fallaron o hubo un error en la ejecución!")
    print("="*30)

# Bloque principal para demostrar el uso de las funciones
if __name__ == "__main__":
   # Ahora, este script ejecutará directamente las pruebas.
   ejecutar_tests()