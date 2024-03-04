import ply.lex as lex

# Lista de palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'print': 'PRINT'
}

# Lista de nombres de tokens
tokens = [
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON'
] + list(reserved.values())

# Reglas para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'

# Regla para identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Verifica palabras reservadas
    return t

# Regla para números (enteros y decimales)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Regla para manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres a ignorar (espacios y tabulaciones)
t_ignore = ' \t'

# Regla para manejar errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construye el lexer
lexer = lex.lex()

# Función para analizar un archivo de entrada
def analyze(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)

# Llama a la función con la ruta de tu archivo
analyze('./codigo_fuente_ejemplo.txt')
