import ply.yacc as yacc
from analizadorLexico import tokens
from analizadorSemantico import SymbolTable

symbol_table = SymbolTable()

precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
)

def p_program(p):
    'program : declaration_list'
    p[0] = ('program', p[1])

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_declaration(p):
    '''declaration : var_declaration
                   | fun_declaration
                   | class_declaration'''
    p[0] = p[1]

def p_var_declaration(p):
    '''var_declaration : type_specifier IDENTIFICADOR PUNTOYCOMA
                       | type_specifier IDENTIFICADOR ASIGNACION expression PUNTOYCOMA'''
    if len(p) == 4:
        p[0] = ('var_decl', p[1], p[2])
    elif len(p) == 6:
        p[0] = ('var_decl', p[1], p[2], p[4])

def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | IDENTIFICADOR'''
    p[0] = p[1]

def p_fun_declaration(p):
    'fun_declaration : type_specifier IDENTIFICADOR LPAREN param_list RPAREN compound_statement'
    p[0] = ('fun_decl', p[1], p[2], p[4], p[6])

def p_param_list(p):
    '''param_list : param_list COMA param
                  | param
                  | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_param(p):
    'param : type_specifier IDENTIFICADOR'
    p[0] = ('param', p[1], p[2])

def p_class_declaration(p):
    'class_declaration : CLASS IDENTIFICADOR LBRACE declaration_list RBRACE'
    p[0] = ('class_decl', p[2], p[4])

def p_compound_statement(p):
    'compound_statement : LBRACE statement_list RBRACE'
    p[0] = ('compound_stmt', p[2])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_statement(p):
    '''statement : declaration
                 | var_declaration
                 | expression_statement
                 | compound_statement
                 | selection_statement
                 | iteration_statement
                 | return_statement'''
    p[0] = p[1]

def p_expression_statement(p):
    'expression_statement : expression PUNTOYCOMA'
    p[0] = p[1]

def p_selection_statement(p):
    '''selection_statement : IF LPAREN expression RPAREN statement
                           | IF LPAREN expression RPAREN statement ELSE statement'''
    if len(p) == 6:
        p[0] = ('if', p[3], p[5])
    else:
        p[0] = ('if_else', p[3], p[5], p[7])

def p_iteration_statement(p):
    '''iteration_statement : WHILE LPAREN expression RPAREN statement
                           | FOR LPAREN expression_statement expression_statement expression RPAREN statement'''
    if len(p) == 6:
        p[0] = ('while', p[3], p[5])
    else:
        p[0] = ('for', p[3], p[4], p[5], p[7])

def p_return_statement(p):
    'return_statement : RETURN expression PUNTOYCOMA'
    p[0] = ('return', p[2])

def p_expression(p):
    '''expression : simple_expression
                  | IDENTIFICADOR ASIGNACION expression
                  | IDENTIFICADOR DOT IDENTIFICADOR
                  | IDENTIFICADOR DOT IDENTIFICADOR LPAREN arg_list RPAREN'''
    if len(p) == 4:
        if p[2] == '=':
            p[0] = ('assign', p[1], p[3])
        else:
            p[0] = ('access_member', p[1], p[3])
    elif len(p) == 2:
        p[0] = p[1]
    elif len(p) == 6:
        p[0] = ('method_call', p[1], p[3], p[5])

def p_simple_expression(p):
    '''simple_expression : simple_expression SUMA term
                         | simple_expression RESTA term
                         | term'''
    if len(p) == 4:
        p[0] = ('binop', p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term MULTIPLICACION factor
            | term DIVISION factor
            | factor'''
    if len(p) == 4:
        p[0] = ('binop', p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : IDENTIFICADOR
              | ENTERO
              | REAL
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        if isinstance(p[1], int) or isinstance(p[1], float):
            p[0] = ('number', p[1])
        elif isinstance(p[1], str):
            p[0] = ('var', p[1])
        else:
            p[0] = p[1]
    else:
        p[0] = p[2]

def p_call(p):
    'call : IDENTIFICADOR LPAREN arg_list RPAREN'
    p[0] = ('call', p[1], p[3])

def p_arg_list(p):
    '''arg_list : arg_list COMA expression
                | expression
                | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_empty(p):
    'empty :'
    p[0] = None

def p_access_member(p):
    'access_member : IDENTIFICADOR DOT IDENTIFICADOR'
    p[0] = ('access_member', p[1], p[3])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', type {p.type}, at line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
