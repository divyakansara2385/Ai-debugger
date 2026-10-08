import os
import shutil
import tempfile
from git import Repo


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


def clone_repository(repo_url):
    """
    Clone only the latest version of a repository.
    """

    temp_dir = tempfile.mkdtemp()

    try:
        Repo.clone_from(
            repo_url,
            temp_dir,
            depth=1
        )

        return temp_dir

    except Exception as e:
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise Exception(f"Could not clone repository: {e}")


def get_source_files(repo_path):
    """
    Scan repository and return supported source-code files.
    """

    source_files = []

    for root, dirs, files in os.walk(repo_path):

        # Ignore unnecessary folders
        dirs[:] = [
            d for d in dirs
            if d not in {
                ".git",
                "__pycache__",
                "node_modules",
                "venv",
                ".venv"
            }
        ]

        for file in files:

            extension = os.path.splitext(file)[1].lower()

            if extension in SUPPORTED_EXTENSIONS:

                file_path = os.path.join(root, file)

                source_files.append({
                    "path": file_path,
                    "language": SUPPORTED_EXTENSIONS[extension]
                })

    return source_files