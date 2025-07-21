import pytest
from calculadora import sumar, restar

# Códigos de color ANSI para la salida en la terminal
VERDE = '\033[92m'
ROJO = '\033[91m'
RESET = '\033[0m'

@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),      # Positivos
    (-1, 1, 0),     # Negativo y positivo
    (-5, -5, -10),  # Negativos
    (0, 0, 0),      # Ceros
    (100, 200, 300) # Números grandes
])
def test_sumar(a, b, esperado):
    """Prueba la función sumar con múltiples casos, imprimiendo su estado."""
    print(f"\nProbando suma: {a} + {b}")
    resultado = sumar(a, b)
    print(f"  - Esperado: {esperado}, Obtenido: {resultado}")
    try:
        assert resultado == esperado
        print(f"  - Estado: {VERDE}PASÓ ✅{RESET}")
    except AssertionError:
        print(f"  - Estado: {ROJO}FALLÓ ❌{RESET}")
        raise  # Re-lanza la excepción para que pytest marque el test como fallido

@pytest.mark.parametrize("a, b, esperado", [
    (10, 5, 5),     # Positivos
    (-1, 1, -2),    # Negativo y positivo
    (5, 10, -5),    # Resultado negativo
    (0, 0, 0),      # Ceros
    (-5, -10, 5)    # Resta de negativos
])
def test_restar(a, b, esperado):
    """Prueba la función restar con múltiples casos, imprimiendo su estado."""
    print(f"\nProbando resta: {a} - {b}")
    resultado = restar(a, b)
    print(f"  - Esperado: {esperado}, Obtenido: {resultado}")
    try:
        assert resultado == esperado
        print(f"  - Estado: {VERDE}PASÓ ✅{RESET}")
    except AssertionError:
        print(f"  - Estado: {ROJO}FALLÓ ❌{RESET}")
        raise  # Re-lanza la excepción para que pytest marque el test como fallido