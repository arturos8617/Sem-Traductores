import ast
import graphviz

# Función para visualizar el árbol sintáctico
def visualize_ast(node, graph=None, node_counts=None, parent_name=None):
    if graph is None:
        graph = graphviz.Digraph('AST', node_attr={'shape': 'ellipse'}, format='png')
    if node_counts is None:
        node_counts = {}

    if isinstance(node, ast.AST):
        node_type = type(node).__name__
        # Incrementar el conteo para el tipo de nodo o inicializarlo si aún no existe
        count = node_counts.get(node_type, 0) + 1
        node_counts[node_type] = count
        
        # Crear una etiqueta única para el nodo
        name = f'{node_type}{count}'
        graph.node(name, label=node_type)
        
        # Conectar este nodo con su padre si es que existe
        if parent_name is not None:
            graph.edge(parent_name, name)
        
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    visualize_ast(item, graph, node_counts, parent_name=name)
            elif isinstance(value, ast.AST):
                visualize_ast(value, graph, node_counts, parent_name=name)

    return graph

# Ruta al archivo de código fuente
file_path = 'example_code.txt'  # Asegúrate de que la ruta al archivo y su nombre sean correctos.

# Leer el código fuente desde el archivo
with open(file_path, 'r') as source_file:
    code = source_file.read()

# Construir el AST
parsed_code = ast.parse(code)

# Visualizar el AST
graph = visualize_ast(parsed_code)
graph.view()  # Esto abrirá el gráfico directamente sin guardar un archivo
