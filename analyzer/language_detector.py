import os


SUPPORTED_EXTENSIONS = {
    ".py": "Python",
    ".java": "Java",
    ".c": "C",
    ".cpp": "C++",
    ".h": "C/C++ Header",
    ".hpp": "C++ Header",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".html": "HTML",
    ".css": "CSS"
}


def detect_language(file_path):
    """
    Detect the programming language from the file extension.
    """

    extension = os.path.splitext(file_path)[1].lower()

    return SUPPORTED_EXTENSIONS.get(extension, "Unknown")