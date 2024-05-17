class CodeGenerator:
    def __init__(self):
        self.code = []

    def generate(self, node):
        method_name = f'generate_{node[0]}'
        method = getattr(self, method_name, self.generic_generate)
        return method(node)

    def generic_generate(self, node):
        raise Exception(f'No generate_{node[0]} method')

    def generate_program(self, node):
        for child in node[1]:
            self.generate(child)
        return '\n'.join(self.code)

    def generate_assign(self, node):
        _, var_name, expr = node
        self.code.append(f'{var_name} = {self.generate(expr)}')

    def generate_binop(self, node):
        _, left, op, right = node
        left_code = self.generate(left)
        right_code = self.generate(right)
        return f'({left_code} {op} {right_code})'

    def generate_number(self, node):
        return str(node[1])

    def generate_var(self, node):
        return node[1]
