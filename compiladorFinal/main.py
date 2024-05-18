import ply.yacc as yacc
from analizadorLexico import lexer  # Importa el lexer ya construido
from analizadorSintactico import parser
from analizadorSemantico import SemanticAnalyzer  # Importa SemanticAnalyzer
from generadorCodigo import CodeGenerator

# Paso 1: Análisis Léxico
with open('programa.txt', 'r') as file:
    data = file.read()

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

# Paso 2: Análisis Sintáctico
ast = parser.parse(data, lexer=lexer)
print("AST:", ast)

# Paso 3: Análisis Semántico
semantic_analyzer = SemanticAnalyzer()  # Asegúrate de que estás creando una instancia de SemanticAnalyzer
semantic_analyzer.analyze(ast)


# Paso 4: Generación de Código
generator = CodeGenerator()
python_code = generator.generate(ast)
print("Código Generado:")
print(python_code)

# Guardar el código generado en un archivo
with open('programa_generado.py', 'w') as output_file:
    output_file.write(python_code)

# Opcional: Ejecutar el código generado
exec(python_code)
