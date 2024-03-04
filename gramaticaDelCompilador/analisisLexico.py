import re

# Definir un diccionario con expresiones regulares para identificar cada token
# Nota: Este es un esqueleto básico, las expresiones regulares pueden necesitar ajustes
token_regex = {
    'identificador': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'entero': r'\b\d+\b',
    'real': r'\b\d+\.\d+\b',
    'cadena': r'"[^"]*"',
    'tipo': r'\b(int|float|string|bool)\b',
    'opSuma': r'[+-]',
    'opMul': r'[*/]',
    'opRelac': r'(<|>|<=|>=|==|!=)',
    'opOr': r'\|\|',
    'opAnd': r'&&',
    'opNot': r'!',
    'opIgualdad': r'==',
    ';': r';',
    ',': r',',
    '(': r'\(',
    ')': r'\)',
    '{': r'\{',
    '}': r'\}',
    '=': r'=',
    'if': r'\bif\b',
    'while': r'\bwhile\b',
    'return': r'\breturn\b',
    'else': r'\belse\b',
    '$': r'\$'
}

# Función para el analizador léxico
def lexer(input_text):
    tokens = []
    while input_text:
        match = None
        for token_type, regex in token_regex.items():
            regex_match = re.match(regex, input_text)
            if regex_match:
                match = regex_match.group(0)
                tokens.append((token_type, match))
                input_text = input_text[len(match):].lstrip()  # Eliminar el token encontrado y espacios iniciales
                break
        if not match:
            raise ValueError(f"Error léxico en: {input_text}")
    return tokens

# Ejemplo de uso del analizador léxico
example_code = "int suma = 5 + 3;"
lexer_output = lexer(example_code)

# Mostrar los tokens identificados
lexer_output
