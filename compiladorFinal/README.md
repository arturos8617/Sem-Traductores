# Mi Compilador

Este proyecto es un compilador que traduce un lenguaje de programación personalizado a código Python. El compilador realiza análisis léxico, sintáctico y semántico, y genera un archivo Python que puede ser ejecutado o convertido a un ejecutable.

## Características
- **Análisis Léxico**: Convierte el código fuente en una lista de tokens.
-**Análisis Sintáctico**: Construye un árbol de sintaxis abstracta (AST) a partir de los tokens.
-**Análisis Semántico**: Verifica la validez semántica del código, como la declaración de variables y tipos de datos.
-**Generación de Código**: Genera un script Python a partir del AST.

## Requisitos
- Python 3.x

## Instalación
1. Clona el repositorio:
```sh
git clone https://github.com/tu-usuario/mi-compilador.git
cd mi-compilador
```

2. Instala las dependencias necesarias (si las hay).

## Uso
1. Preparar el archivo fuente: Asegúrate de que tu código fuente está en el archivo programa.txt.

2. Ejecutar el compilador:
```sh
python main.py
```
Esto ejecutará el compilador, que realizará los siguientes pasos:

- Análisis Léxico
- Análisis Sintáctico
- Análisis Semántico
- Generación de Código
3. Verificar el código generado: Si no hay errores, el compilador generará un archivo llamado ´programagenerado.py´.

4. Ejecutar el código Python generado (opcional):

```sh 
python programagenerado.py
```
5.Convertir a un ejecutable (opcional):

Si deseas convertir el script Python generado en un ejecutable, puedes usar PyInstaller.
Primero, instala PyInstaller:

```sh
pip install pyinstaller
```
Luego, convierte el script a un ejecutable:
```sh
pyinstaller --onefile programagenerado.py
```
El ejecutable se generará en el directorio ´dist´.

## Estructura del Proyecto
- **main.py**: El punto de entrada del compilador.
- **analizadorLexico.py**: Realiza el análisis léxico.
- **analizadorSintactico.py**: Realiza el análisis sintáctico.
- **analizadorSemantico.py**: Realiza el análisis semántico.
- **generadorCodigo.py**: Genera el código Python.
- **programa.txt**: El archivo de código fuente a ser compilado.
- **programagenerado.py**: El archivo de código Python generado.

## Ejemplo de Código Fuente
Ejemplo de código en programa.txt:

```cpp
int main() {
    int x = 1 + 2;
    int y = 5 * 3;
    return y;
}
```
## Mensajes de Error
Si se encuentra algún error durante el proceso de compilación, se mostrará un mensaje de error indicando el tipo de error y su ubicación en el código fuente.

## Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes sugerencias, por favor abre un issue o envía un pull request.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
