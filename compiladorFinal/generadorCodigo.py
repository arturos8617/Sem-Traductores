class CodeGenerator:
    def __init__(self):
        self.code = []

    def generate(self, node):
        self.visit(node)
        return "\n".join(self.code)

    def visit(self, node):
        if node is None:
            return
        if isinstance(node, tuple) and isinstance(node[0], str):
            method_name = f'generate_{node[0]}'
            method = getattr(self, method_name, self.generic_generate)
            method(node)
        elif isinstance(node, list):
            for item in node:
                if item is not None:
                    self.visit(item)
        else:
            self.generic_generate(node)

    def generic_generate(self, node):
        raise Exception(f'No generate_{node} method')

    def generate_program(self, node):
        self.visit(node[1])

    def generate_fun_decl(self, node):
        _, return_type, fun_name, params, body = node
        param_str = ", ".join([f"{p[1]}" for p in params if p is not None])
        self.code.append(f"def {fun_name}({param_str}):")
        self.visit(body)
        self.code.append("")  # Añadir una línea en blanco después de la función

    def generate_compound_stmt(self, node):
        for statement in node[1]:
            self.visit(statement)

    def generate_var_decl(self, node):
        if len(node) == 3:
            _, var_type, var_name = node
            self.code.append(f"    {var_name} = None")
        elif len(node) == 4:
            _, var_type, var_name, expr = node
            self.code.append(f"    {var_name} = {self.expr_to_code(expr)}")

    def generate_assign(self, node):
        _, var_name, expr = node
        self.code.append(f"    {var_name} = {self.expr_to_code(expr)}")

    def generate_binop(self, node):
        _, left, op, right = node
        return f"({self.expr_to_code(left)} {op} {self.expr_to_code(right)})"

    def generate_number(self, node):
        return str(node[1])

    def generate_var(self, node):
        return node[1]

    def generate_return(self, node):
        _, expr = node
        self.code.append(f"    return {self.expr_to_code(expr)}")

    def expr_to_code(self, expr):
        if expr[0] == 'binop':
            return self.generate_binop(expr)
        elif expr[0] == 'number':
            return self.generate_number(expr)
        elif expr[0] == 'var':
            return self.generate_var(expr)
        else:
            self.visit(expr)

# Prueba del generador de código
if __name__ == "__main__":
    # Ejemplo de AST para prueba
    ast = ('program', [
        ('fun_decl', 'int', 'main', [None], ('compound_stmt', [
            ('var_decl', 'int', 'x', ('binop', ('number', 1), '+', ('number', 2))),
            ('var_decl', 'int', 'y', ('binop', ('number', 5), '*', ('number', 3))),
            ('assign', 'x', ('binop', ('var', 'x'), '*', ('number', 3))),
            ('return', ('var', 'y'))
        ]))
    ])

    generator = CodeGenerator()
    try:
        python_code = generator.generate(ast)
        print("Código Generado:")
        print(python_code)
    except Exception as e:
        print(f"Error de generación de código: {e}")
