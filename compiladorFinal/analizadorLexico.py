import ply.lex as lex

tokens = [
    'IDENTIFICADOR', 'ENTERO', 'REAL', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION',
    'ASIGNACION', 'MENOR', 'MAYOR', 'MENORIGUAL', 'MAYORIGUAL', 'NOIGUAL', 'IGUAL',
    'AND', 'OR', 'NOT', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'PUNTOYCOMA', 'COMA', 
    'IF', 'ELSE', 'WHILE', 'FOR', 'INT', 'FLOAT', 'CLASS', 'RETURN', 'DOT'
]

# Tokens de operadores y símbolos
t_SUMA    = r'\+'
t_RESTA   = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='
t_MENOR   = r'<'
t_MAYOR   = r'>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_NOIGUAL = r'!='
t_IGUAL   = r'=='
t_AND     = r'&&'
t_OR      = r'\|\|'
t_NOT     = r'!'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_PUNTOYCOMA = r';'
t_COMA    = r','
t_DOT     = r'\.'

# Ignorar espacios y tabulaciones
t_ignore = ' \t\n'

# Definiciones de tokens complejos
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = {'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'for': 'FOR', 'int': 'INT', 'float': 'FLOAT', 'class': 'CLASS', 'return': 'RETURN'}.get(t.value.lower(), 'IDENTIFICADOR')
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)  # Convertir el valor a entero
    return t

def t_REAL(t):
    r'\d*\.\d+|\d+\.\d*'
    t.value = float(t.value)  # Convertir el valor a real
    return t

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()


