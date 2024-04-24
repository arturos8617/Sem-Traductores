import ast
import graphviz

# Función para visualizar el árbol sintáctico
def visualize_ast(node, graph=None):
    if graph is None:
        graph = graphviz.Digraph('AST', node_attr={'shape': 'rectangle'})
        
    if isinstance(node, ast.AST):
        name = f'{type(node).__name__}-{id(node)}'
        graph.node(name, label=type(node).__name__)
        
        for field, value in ast.iter_fields(node):
            value_name = f'{field}-{id(value)}'
            graph.node(value_name, label=str(value))
            graph.edge(name, value_name)
            
            if isinstance(value, list):
                for item in value:
                    child_name = f'{type(item).__name__}-{id(item)}'
                    visualize_ast(item, graph)
                    graph.edge(value_name, child_name)
            elif isinstance(value, ast.AST):
                child_name = f'{type(value).__name__}-{id(value)}'
                visualize_ast(value, graph)
                graph.edge(value_name, child_name)

    return graph

# Ruta al archivo de código fuente
file_path = './example_code.txt'

# Leer el código fuente desde el archivo
with open(file_path, 'r') as source_file:
    code = source_file.read()

# Construir el AST
parsed_code = ast.parse(code)

# Visualizar el AST
graph = visualize_ast(parsed_code)
graph.render('ast-graph', view=True)  # Esto guardará y abrirá el archivo .pdf del gráfico
