from analyzer.code_parser import parse_python_code
from analyzer.error_detector import detect_errors


code = """
x = 10
print(y)
"""


result = parse_python_code(code)


if result["success"]:

    errors = detect_errors(result["tree"])

    print("\nErrors found:\n")

    for error in errors:
        print(error)

else:
    print("Syntax error:")
    print(result["error"])