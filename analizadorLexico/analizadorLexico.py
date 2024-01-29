import re

# Defining a class for the lexical analyzer
class LexicalAnalyzer:
    def __init__(self):
        # Define regular expressions for each token type
        self.token_patterns = {
            'INTEGER': r'\b\d+\b',
            'REAL': r'\b\d+\.\d+\b',
            'ID': r'\b[a-zA-Z_][a-zA-Z_0-9]*\b',
            'ADD_OP': r'\+',
            'MUL_OP': r'\*',
            'ASSIGN_OP': r'=',
            'REL_OP': r'(==|!=|<=|>=|<|>)',
            'LOGIC_OP': r'(\band\b|\bor\b|\bnot\b)',
            'PARENTHESIS': r'(\(|\))',
            'BRACES': r'({|})',
            'SEMICOLON': r';',
            'IF': r'\bif\b',
            'WHILE': r'\bwhile\b',
            'RETURN': r'\breturn\b',
            'ELSE': r'\belse\b',
            'INT': r'\bint\b',
            'FLOAT': r'\bfloat\b'
        }

    def tokenize(self, code):
        # Tokenize the input code
        tokens = []
        for token_type, pattern in self.token_patterns.items():
            for match in re.finditer(pattern, code):
                tokens.append((token_type, match.group(), match.start()))
        # Sort tokens by their position in the code
        return sorted(tokens, key=lambda x: x[2])

# Example code snippet
code_snippet = "int x = 10; if (x > 0) { x = x + 1.5; }"

# Create a lexical analyzer and tokenize the code snippet
analyzer = LexicalAnalyzer()
tokens = analyzer.tokenize(code_snippet)

# Display the tokens
print(tokens)

