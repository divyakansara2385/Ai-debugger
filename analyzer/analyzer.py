from analyzer.code_extractor import extract_code
from analyzer.code_parser import parse_python_code
from analyzer.error_detector import detect_errors
from analyzer.nlp_processor import explain_error


def analyze_file(file_path):
    """
    Analyze a single source-code file.
    """

    # Step 1: Extract code
    file_data = extract_code(file_path)

    language = file_data["language"]
    code = file_data["content"]

    # Step 2: Currently analyze Python files
    if language != "Python":
        return {
            "path": file_path,
            "language": language,
            "errors": [],
            "message": "Detailed analysis is currently available for Python files."
        }

    # Step 3: Parse code
    parse_result = parse_python_code(code)

    if not parse_result["success"]:
        return {
            "path": file_path,
            "language": language,
            "errors": [
                {
                    "type": "SyntaxError",
                    "message": parse_result["error"]["message"],
                    "line": parse_result["error"]["line"],
                    "explanation": (
                        f"A syntax error was found on line "
                        f"{parse_result['error']['line']}: "
                        f"{parse_result['error']['message']}"
                    )
                }
            ]
        }

    # Step 4: Detect errors
    errors = detect_errors(parse_result["tree"])

    # Step 5: Add NLP explanation, suggested fix and similarity
    for error in errors:

        nlp_result = explain_error(error)

        error["explanation"] = nlp_result["explanation"]

        error["suggested_fix"] = nlp_result["suggested_fix"]

        error["similarity"] = nlp_result["similarity"]

    return {
        "path": file_path,
        "language": language,
        "errors": errors
    }