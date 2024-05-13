class SymbolTable:
    def __init__(self):
        self.scopes = [{}]

    def enter_scope(self):
        # Crea un nuevo ámbito al entrar a un bloque
        self.scopes.append({})

    def exit_scope(self):
        # Sale del ámbito actual al salir de un bloque
        if len(self.scopes) > 1:
            self.scopes.pop()

    def declare(self, name, symbol_info):
        # Declara un nuevo símbolo en el ámbito actual
        if name in self.scopes[-1]:
            raise Exception(f"Variable '{name}' is already declared in this scope.")
        self.scopes[-1][name] = symbol_info

    def lookup(self, name):
        # Busca un símbolo en los ámbitos disponibles, del más cercano al más lejano
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Variable '{name}' is not declared.")

# Uso de la tabla de símbolos
symbol_table = SymbolTable()
symbol_table.enter_scope()
symbol_table.declare('x', {'type': 'int', 'initialized': True})
print(symbol_table.lookup('x'))
symbol_table.exit_scope()
