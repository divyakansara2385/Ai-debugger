from analyzer.language_detector import detect_language


files = [
    "main.py",
    "App.java",
    "calculator.cpp",
    "script.js",
    "index.html",
    "style.css",
    "README.md"
]


for file in files:
    language = detect_language(file)
    print(file, "→", language)