# Ejemplos de Código - Estructura de Datos y Programación (ITBA)

Este repositorio contiene ejemplos de código en Python utilizados en la materia **Estructura de Datos y Programación** del ITBA. Los ejemplos están organizados por temas y clases, y cubren conceptos fundamentales de programación y estructuras de datos.

## Estructura del repositorio

Cada carpeta contiene archivos `.py` con el código visto en clase, y puede incluir un archivo `main.py` para ejecutar ejemplos completos.

## Cómo usar los ejemplos

1. Clona este repositorio:
	```zsh
	git clone https://github.com/cmaceira-itba/edyp-s2-2025-b.git
	```
2. Ingresa a la carpeta del repositorio:
	```zsh
	cd edyp-s2-2025-b
	```
3. Ejecuta los ejemplos desde la terminal:
	```zsh
	python3 gestion_biblioteca/main.py
	python3 gestion_camiones/main.py
	python3 funcional/funcional.py
	```

## Requisitos

- Python 3.10 o superior

## Propósito

Este repositorio sirve como material de apoyo y referencia para los estudiantes de la materia, facilitando la práctica y el repaso de los conceptos vistos en clase.

## Instrucciones de Ejecución de ejemplo numpy

### Prerequisitos
- Tener uv (instalador de paquetes y gestor de proyectos para Python) instalado. Si no lo tenés, podés instalarlo siguiendo las instrucciones en https://uvlang.org/.
- Tener Python 3.10 o superior instalado.

### Ejecución del ejemplo

Para ejecutar este ejemplo, asegurate de tener las dependencias instaladas en tu proyecto:
```bash
# Instalar dependencias (si no las tenés)
uv add opencv-python numpy

# Ejecutar el script
uv run numpy/ejemplo.py
```

**Nota:** Si querés usar una imagen propia en lugar de la generada sintéticamente, colocá un archivo llamado `imagen.jpg` en la raíz del proyecto (donde está el `pyproject.toml`) antes de ejecutar el script.

---

**Autor:** Carlos Maceira
**Materia:** Estructura de Datos y Programación
**Instituto Tecnológico de Buenos Aires (ITBA)**
**Año:** 2025
