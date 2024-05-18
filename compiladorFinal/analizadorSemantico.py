class SymbolTable:
    def __init__(self):
        self.scopes = [{}]

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def declare(self, name, symbol_info):
        if name in self.scopes[-1]:
            raise Exception(f"Variable '{name}' is already declared in this scope.")
        self.scopes[-1][name] = symbol_info

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Variable '{name}' is not declared.")

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, ast):
        self.visit(ast)

    def visit(self, node):
        if node is None:
            return
        if isinstance(node, tuple) and isinstance(node[0], str):
            method_name = f'visit_{node[0]}'
            method = getattr(self, method_name, self.generic_visit)
            method(node)
        elif isinstance(node, list):
            for item in node:
                if item is not None:
                    self.visit(item)
        else:
            self.generic_visit(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{node} method")

    def visit_program(self, node):
        self.symbol_table.enter_scope()  # Enter global scope
        self.visit(node[1])
        self.symbol_table.exit_scope()  # Exit global scope

    def visit_var_decl(self, node):
        _, var_type, var_name = node[:3]
        self.symbol_table.declare(var_name, {'type': var_type, 'initialized': False})
        if len(node) == 4:
            self.visit(node[3])  # Visit the expression if initialized

    def visit_assign(self, node):
        _, var_name, expr = node
        self.visit(expr)
        self.symbol_table.lookup(var_name)  # Check if the variable is declared

    def visit_binop(self, node):
        _, left, op, right = node
        self.visit(left)
        self.visit(right)

    def visit_number(self, node):
        pass

    def visit_var(self, node):
        _, var_name = node
        self.symbol_table.lookup(var_name)  # Check if the variable is declared

    def visit_return(self, node):
        _, expr = node
        self.visit(expr)

    def visit_fun_decl(self, node):
        _, return_type, fun_name, params, body = node
        self.symbol_table.declare(fun_name, {'type': 'function', 'return_type': return_type, 'parameters': params})
        self.symbol_table.enter_scope()
        if params != [None]:  # Evitar pasar [None] a visit
            for param in params:
                self.visit(param)
        self.visit(body)
        self.symbol_table.exit_scope()

    def visit_param(self, node):
        _, param_type, param_name = node
        self.symbol_table.declare(param_name, {'type': param_type, 'initialized': True})

    def visit_compound_stmt(self, node):
        for statement in node[1]:
            self.visit(statement)

# Prueba del código del analizador semántico
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

    semantic_analyzer = SemanticAnalyzer()
    try:
        semantic_analyzer.analyze(ast)
        print("Análisis semántico completado sin errores.")
    except Exception as e:
        print(f"Error de análisis semántico: {e}")
