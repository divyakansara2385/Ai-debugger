from analyzer.code_parser import parse_python_code


code = """
x = 10
print(x
"""


result = parse_python_code(code)

if result["success"]:
    print("Code parsed successfully!")
    print("AST created successfully.")

else:
    print("Error found:")
    print(result["error"])