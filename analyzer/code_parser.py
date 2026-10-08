import ast


def parse_python_code(code):
    """
    Parse Python source code into an Abstract Syntax Tree.
    """

    try:
        tree = ast.parse(code)

        return {
            "success": True,
            "tree": tree,
            "error": None
        }

    except SyntaxError as e:
        return {
            "success": False,
            "tree": None,
            "error": {
                "type": "SyntaxError",
                "message": e.msg,
                "line": e.lineno,
                "column": e.offset
            }
        }