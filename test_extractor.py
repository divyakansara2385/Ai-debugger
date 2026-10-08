from analyzer.code_extractor import extract_code


file_path = input("Enter source file path: ")

result = extract_code(file_path)

print("\nLanguage:", result["language"])
print("\nCode:")
print(result["content"]) 