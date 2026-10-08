import ast


class UndefinedVariableDetector(ast.NodeVisitor):

    def __init__(self):
        self.defined_variables = set()
        self.errors = []

    def visit_Assign(self, node):
        for target in node.targets:

            if isinstance(target, ast.Name):
                self.defined_variables.add(target.id)

        self.generic_visit(node)

    def visit_Name(self, node):

        if isinstance(node.ctx, ast.Load):

            if node.id not in self.defined_variables:
                self.errors.append({
                    "type": "Undefined Variable",
                    "variable": node.id,
                    "line": node.lineno
                })

        self.generic_visit(node)


def detect_errors(tree):

    detector = UndefinedVariableDetector()

    detector.visit(tree)

    return detector.errors