import re

class Lexer:
    def __init__(self):
        # Mapeo de los tipos de token a su valor numérico según la tabla proporcionada
        self.token_types = {
            'IDENTIFICADOR': 0,
            'ENTERO': 1,
            'REAL': 2,
            'TIPO': 4,  # int, float, void
            'OP_SUMA': 5,  # +, -
            'OP_MULTIPLICACION': 6,  # *, /
            'OP_RELACIONAL': 7,  # <, >, <=, >=
            'OP_OR': 8,  # ||
            'OP_AND': 9,  # &&
            'OP_NOT': 10,  # !
            'OP_IGUALDAD': 11,  # ==, !=
            'PUNTO_Y_COMA': 12,  # ;
            'COMA': 13,  # ,
            'PARENTESIS_ABRE': 14,  # (
            'PARENTESIS_CIERRA': 15,  # )
            'LLAVE_ABRE': 16,  # {
            'LLAVE_CIERRA': 17,  # }
            'OP_ASIGNACION': 18,  # =
            'IF': 19,
            'WHILE': 20,
            'RETURN': 21,
            'ELSE': 22,
            'FIN_DE_ARCHIVO': 23,  # Simbolizado por $
        }

        # Definición de las expresiones regulares para cada tipo de token
        self.token_regex = [
            ('REAL', r'\d+\.\d+|\.\d+'),  # Acepta números con punto decimal al principio
            ('ENTERO', r'\d+'),
            ('IDENTIFICADOR', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('TIPO', r'\b(int|float|void)\b'),
            ('OP_SUMA', r'[+-]'),
            ('OP_MULTIPLICACION', r'[*\/]'),
            ('OP_RELACIONAL', r'<=|>=|==|!=|<|>'),
            ('OP_OR', r'\|\|'),
            ('OP_AND', r'&&'),
            ('OP_NOT', r'!'),
            ('OP_IGUALDAD', r'==|!='),
            ('PUNTO_Y_COMA', r';'),
            ('COMA', r','),
            ('PARENTESIS_ABRE', r'\('),
            ('PARENTESIS_CIERRA', r'\)'),
            ('LLAVE_ABRE', r'{'),
            ('LLAVE_CIERRA', r'}'),
            ('OP_ASIGNACION', r'='),  # La asignación simple no necesita una expresión compleja
            ('IF', r'\bif\b'),
            ('WHILE', r'\bwhile\b'),
            ('RETURN', r'\breturn\b'),
            ('ELSE', r'\belse\b'),
            ('FIN_DE_ARCHIVO', r'\$'),
        ]

    def tokenize(self, code):
        # Separación y clasificación de tokens
        tokens = []
        pos = 0
        while pos < len(code):
            match = None
            # Ignorar espacios en blanco
            if re.match(r'\s', code[pos]):
                pos += 1
                continue
            for token_name, token_regex in self.token_regex:
                regex = re.compile(token_regex)
                match = regex.match(code, pos)
                if match:
                    token_value = match.group(0)
                    token_type = self.token_types[token_name]
                    tokens.append((token_type, token_value))
                    pos = match.end()
                    break
            if not match:
                raise SyntaxError(f'Error de sintaxis cerca de: {code[pos:]}')
        return tokens

# Ejemplo de uso
lexer = Lexer()
code = "if (a >= .5) { int x = y + 2; } else { x = x - 1; } $"
print(lexer.tokenize(code))
