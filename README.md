# Calculadora con Pruebas Integradas en Pytest

Este es un proyecto simple de una calculadora en Python que demuestra la integración de pruebas unitarias con `pytest` de una manera interactiva y auto-contenida.

## Características

- **Funciones básicas de calculadora**: Suma y resta.
- **Pruebas unitarias robustas**: Utiliza `pytest` y su decorador `@pytest.mark.parametrize` para probar múltiples casos de manera eficiente.
- **Ejecución de pruebas automatizada**: El script principal puede instalar dependencias y ejecutar las pruebas con un solo comando.
- **Instalación automática de dependencias**: Al ejecutar el script, se asegura de que `pytest` esté instalado usando el archivo `requirements.txt`.
- **Salida de pruebas descriptiva**: Los tests imprimen en la consola qué están haciendo y si pasan o fallan, usando colores para una fácil lectura.

---

## Estructura del Proyecto

```
pytest/
├── calculadora.py
├── test_calculadora.py
├── requirements.txt
└── README.md
```

- **`calculadora.py`**: El script principal. Contiene la lógica de la calculadora (`sumar`, `restar`) y una función especial (`ejecutar_tests`) que orquesta la instalación de dependencias y la ejecución de las pruebas.
- **`test_calculadora.py`**: Contiene todos los tests unitarios para las funciones de la calculadora.
- **`requirements.txt`**: Define las dependencias del proyecto (en este caso, solo `pytest`).
- **`README.md`**: Este archivo, con la documentación del proyecto.

---

## Instalación

1.  Clona o descarga este repositorio en tu máquina local.

2.  Es altamente recomendable crear y activar un **entorno virtual** para aislar las dependencias del proyecto.
    ```bash
    # Crea el entorno virtual
    python -m venv venv

    # Actívalo en Windows
    .\venv\Scripts\activate

    # Actívalo en macOS/Linux
    source venv/bin/activate
    ```

3.  No es necesario instalar las dependencias manualmente. El script principal se encargará de ello.

---

## Cómo Ejecutar las Pruebas

Este proyecto está diseñado para ser muy fácil de probar.

### Método 1: Ejecución a través del script principal (Recomendado)

Simplemente ejecuta el script `calculadora.py` desde tu terminal. Este comando hará dos cosas:
1.  Instalará `pytest` si no está presente en tu entorno.
2.  Ejecutará todos los tests y te mostrará la salida detallada.

```bash
python calculadora.py
```

### Método 2: Ejecución directa con Pytest

Si ya tienes `pytest` instalado y prefieres el método estándar, puedes ejecutarlo directamente. Usa el flag `-s` para poder ver los mensajes personalizados que hemos añadido en los tests.

```bash
pytest -s
```