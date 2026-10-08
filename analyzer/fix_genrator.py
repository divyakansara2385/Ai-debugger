def generate_fix(error):
    """
    Generate a simple suggested fix for a detected error.
    """

    error_type = error["type"]
    variable = error.get("variable")

    if error_type == "Undefined Variable":

        return (
            f"Define the variable '{variable}' before using it, "
            f"or check whether you meant to use a different variable name."
        )

    return "No suggested fix is available."