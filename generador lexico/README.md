
# Analizador Léxico Simple

Este proyecto incluye un analizador léxico simple escrito en Python. Un analizador léxico es una pieza fundamental de los compiladores, cuya función es leer el código fuente y dividirlo en una secuencia de tokens.

## Tokens

Los tokens son las unidades básicas de construcción de un lenguaje de programación, como palabras clave, identificadores, símbolos y constantes. En este analizador léxico, se reconocen los siguientes tokens:

- Identificadores: Nombres de variables y funciones.
- Números enteros y reales.
- Operadores de adición (`+`, `-`).
- Operadores de multiplicación (`*`, `/`).
- Operadores de asignación (`=`).
- Operadores relacionales (`<`, `>`, `<=`, `>=`, `!=`, `==`).
- Operadores lógicos (`&&`, `||`, `!`).
- Símbolos de puntuación y agrupación como paréntesis (`(`, `)`), llaves (`{`, `}`) y punto y coma (`;`).
- Palabras reservadas del lenguaje (`if`, `while`, `return`, `else`, `int`, `float`).

Cada token identificado se asocia con un valor numérico específico que se utiliza en el análisis sintáctico posterior.

## Uso

Para utilizar el analizador léxico, simplemente se necesita instanciar la clase `Lexer` y llamar al método `tokenize` con una cadena de código fuente como argumento. El método devuelve una lista de tokens identificados con su tipo numérico correspondiente.

```python
lexer = Lexer()
code = "if (a >= 3.5) { int x = y + 2; }"
tokens = lexer.tokenize(code)
print(tokens)
```

## Errores de Sintaxis

Si el analizador léxico encuentra caracteres o secuencias de caracteres que no puede reconocer como un token válido, lanzará un `SyntaxError` con información sobre la ubicación del error en el código.

## Extensibilidad

El analizador puede ser extendido para reconocer más tokens o para cambiar el comportamiento con el que maneja los tokens actuales. Esto se puede hacer agregando o modificando las expresiones regulares y el mapeo de tipos de token en la clase `Lexer`.

---

Este archivo `README.md` proporciona una visión general del analizador léxico. Para más detalles, se puede revisar el código fuente y los comentarios incluidos en el mismo.
