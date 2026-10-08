from analyzer.language_detector import detect_language


def extract_code(file_path):
    """
    Read a source-code file and return its content.
    """

    language = detect_language(file_path)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return {
            "path": file_path,
            "language": language,
            "content": content
        }

    except UnicodeDecodeError:
        return {
            "path": file_path,
            "language": language,
            "content": None
        }