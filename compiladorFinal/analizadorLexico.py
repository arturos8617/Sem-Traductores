import ply.lex as lex

tokens = [
    'IDENTIFICADOR', 'ENTERO', 'REAL', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION',
    'ASIGNACION', 'MENOR', 'MAYOR', 'MENORIGUAL', 'MAYORIGUAL', 'NOIGUAL', 'IGUAL',
    'AND', 'OR', 'NOT', 'PARENTESIS', 'LLAVE', 'PUNTOYCOMA', 'COMA', 'IF', 'ELSE', 
    'WHILE', 'FOR', 'INT', 'FLOAT'
]

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
t_PARENTESIS = r'\(|\)'
t_LLAVE   = r'\{|\}'
t_PUNTOYCOMA = r';'
t_COMA    = r','
t_ignore = ' \t\n'

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = {'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'for': 'FOR', 'int': 'INT', 'float': 'FLOAT'}.get(t.value, 'IDENTIFICADOR')
    return t

def t_ENTERO(t):
    r'\d+'
    return t

def t_REAL(t):
    r'\d*\.\d+|\d+\.\d*'
    return t

def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(len(t.value))

lexer = lex.lex()
