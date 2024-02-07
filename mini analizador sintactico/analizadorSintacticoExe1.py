class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

def analyze_expression_1(expression):
    # Definir la tabla LR(1) aquí basada en la gramática del ejercicio 1
    # Ejemplo: lr_table = {("estado", "entrada"): ("acción", "siguiente_estado")}
    lr_table = {}  # La tabla debe ser completada según el ejercicio

    # Inicializar pila
    stack = Stack()
    stack.push(0)  # Estado inicial

    # Proceso de análisis
    # Este es un esqueleto básico. Se debe adaptar según las operaciones de la tabla LR(1)
    
    print("Análisis completado.")

# Llamar a la función con la cadena a analizar
analyze_expression_1("a+b")
