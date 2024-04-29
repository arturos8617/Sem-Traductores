# Visualizador de Árbol Sintáctico para Python

Este programa es una herramienta para visualizar la estructura de árbol sintáctico abstracto (AST) de código Python. Utiliza el módulo `ast` para generar el AST y `graphviz` para la visualización.

## Requisitos Previos

Antes de ejecutar el programa, asegúrate de tener instalado Python en tu sistema y de haber añadido Graphviz al PATH de tu sistema operativo. Puedes descargar Graphviz desde su [página oficial](https://graphviz.org/download/).

## Instalación

Para instalar las dependencias del programa, ejecuta el siguiente comando:

```bash
pip install graphviz
```

##Para usar el programa, sigue estos pasos:

Prepara tu archivo de código Python:
Escribe el código Python que deseas visualizar en un archivo de texto y guárdalo con la extensión .txt.
Ejecuta el script:

Ejecuta el script visualize_ast.py con la ruta de tu archivo de código Python como argumento:
```python 
visualize_ast.py path_to_your_file.txt
```

El script leerá el código fuente y generará un diagrama del árbol sintáctico.
Ver el resultado:

El script producirá un archivo (por ejemplo, ast-graph.pdf) que contiene la visualización del árbol sintáctico. Abre este archivo con un visor de PDF para ver el resultado.
