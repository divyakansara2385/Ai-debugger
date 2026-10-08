# 🐛 AI Code Debugging Assistant

An **NLP-based code debugging assistant** that analyzes source code, detects potential programming errors, explains them in simple natural language, and provides suggested fixes.

The project combines **static code analysis with Natural Language Processing (NLP)** to make programming errors easier to understand, especially for beginner developers.

---

## 📌 Overview

Debugging can be difficult when error messages are too technical or do not clearly explain what went wrong.

The **AI Code Debugging Assistant** addresses this problem by creating a simple pipeline that:

1. Accepts a GitHub repository.
2. Scans the repository for source-code files.
3. Detects the programming language.
4. Extracts the source code.
5. Parses Python code using the Abstract Syntax Tree (AST).
6. Detects potential programming errors.
7. Uses NLP techniques to identify the most relevant error pattern.
8. Generates a human-readable explanation.
9. Provides a suggested fix.

The main idea is:

> **Static analysis identifies the problem, while NLP helps explain the problem to the developer.**

---

## ✨ Features

* 🔗 **GitHub Repository Analysis**

  * Accepts a GitHub repository URL.
  * Clones the repository for analysis.

* 🔍 **Source File Detection**

  * Scans the repository for supported source-code files.
  * Ignores unnecessary directories such as `.git`, `node_modules`, and virtual environments.

* 🌐 **Language Detection**

  * Identifies languages based on file extensions.
  * Currently recognizes Python, Java, C, C++, JavaScript, TypeScript, HTML, and CSS.

* 🐍 **Python Code Analysis**

  * Uses Python's built-in AST module.
  * Understands the structural representation of Python code.

* ⚠️ **Error Detection**

  * Detects potential issues such as:

    * Undefined variables
    * Syntax errors

* 🧠 **NLP-Based Error Matching**

  * Uses **TF-IDF** to represent error descriptions numerically.
  * Uses **Cosine Similarity** to find the most relevant error pattern.

* 💬 **Natural-Language Explanation**

  * Converts technical error information into understandable explanations.

* 🔧 **Suggested Fixes**

  * Provides guidance for resolving detected errors.

* 🖥️ **Interactive Web Interface**

  * Built using Streamlit.
  * Allows users to enter a repository URL and view analysis results.

---

## 🔄 How It Works

```text
             GitHub Repository
                     │
                     ▼
            Repository Handler
                     │
                     ▼
             Source File Scanner
                     │
                     ▼
              Language Detection
                     │
                     ▼
             Code Extraction
                     │
                     ▼
              Python AST Parser
                     │
                     ▼
              Error Detection
                     │
                     ▼
              Error Information
                     │
                     ▼
              NLP Processing
             ┌───────┴────────┐
             ▼                ▼
           TF-IDF       Cosine Similarity
             └───────┬────────┘
                     ▼
             Error Explanation
                     │
                     ▼
              Suggested Fix
                     │
                     ▼
              Streamlit UI
```

---

## 🧠 NLP Component

The NLP component is an important part of the project.

When an error is detected, the system converts the error information into text.

For example:

```text
Undefined Variable y is used but may not be defined
```

This text is compared with descriptions stored in the error-pattern knowledge base.

### TF-IDF

**TF-IDF (Term Frequency–Inverse Document Frequency)** converts text into numerical vectors based on the importance of words.

This allows the system to represent error descriptions mathematically.

### Cosine Similarity

Cosine similarity measures how similar two text vectors are.

The system compares the detected error with known error descriptions and selects the most relevant pattern.

```text
Detected Error
      ↓
Convert to Text
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Most Similar Error Pattern
      ↓
Explanation + Suggested Fix
```

This provides the NLP layer that connects the technical error detection system with a natural-language explanation.

---

## 🧪 Example

Consider the following Python code:

```python
x = 10
print(y)
```

The system detects:

```text
Type: Undefined Variable
Variable: y
Line: 3
```

The NLP module then generates an explanation such as:

```text
Variable 'y' is being used, but it has not been defined
in the current scope. This may cause a NameError when
the program runs.
```

Suggested fix:

```text
Define the variable 'y' before using it or check whether
you meant to use a different variable name.
```

The system can also display the NLP similarity score used to select the relevant error pattern.

---

## 🛠️ Tech Stack

| Technology       | Purpose                                      |
| ---------------- | -------------------------------------------- |
| **Python**       | Main programming language                    |
| **GitPython**    | GitHub repository cloning and handling       |
| **Python AST**   | Python code parsing and structural analysis  |
| **NLTK**         | Natural Language Processing and tokenization |
| **Scikit-learn** | TF-IDF and cosine similarity                 |
| **Streamlit**    | Interactive web interface                    |
| **JSON**         | Error-pattern knowledge base                 |

---

## 📂 Project Structure

```text
ai-code-debugger/
│
├── app.py
│
├── analyzer/
│   ├── __init__.py
│   ├── repository.py
│   ├── language_detector.py
│   ├── code_extractor.py
│   ├── code_parser.py
│   ├── error_detector.py
│   ├── nlp_processor.py
│   ├── fix_genrator.py
│   └── analyzer.py
│
├── data/
│   └── error_patterns.json
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project

```bash
cd ai-code-debugger
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If required, dependencies can also be installed manually:

```bash
pip install streamlit gitpython nltk scikit-learn
```

---

## ▶️ Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

Enter a GitHub repository URL and click:

```text
Analyze Repository
```

The system will scan the repository and display detected errors, explanations, suggested fixes, and NLP similarity scores.

---

## 🎯 Project Objective

The objective of this project is to build a simple and practical debugging assistant that combines:

**Code Analysis + NLP + Explainable Error Information**

Rather than only displaying technical errors, the system aims to make debugging more understandable by translating detected programming problems into meaningful natural-language explanations.

---

## 🚧 Current Limitations

The current implementation focuses primarily on **Python code analysis**.

Although the system can identify several programming languages based on their file extensions, detailed AST-based error analysis is currently implemented for Python.

The current error detector also focuses on a limited set of error patterns.

---

## 🔮 Future Scope

The project can be extended with:

* Support for Java, C++, JavaScript, and other languages.
* More sophisticated AST-based error detection.
* Detection of additional programming errors.
* Better handling of variable scope.
* More comprehensive error-pattern datasets.
* Code-context-aware explanations.
* Automated code-fix generation.
* Integration with IDEs or GitHub pull requests.
* Repository-level dependency and change analysis.
* More advanced NLP or transformer-based models.

---

## 📚 Learning Outcomes

Through this project, the following concepts are explored:

* Git and repository handling
* Source-code parsing
* Abstract Syntax Trees
* Static code analysis
* Natural Language Processing
* Text preprocessing
* TF-IDF vectorization
* Cosine similarity
* Error-pattern matching
* Explainable debugging
* Streamlit application development

---

## 👩‍💻 Project Concept

**AI Code Debugging Assistant** is designed around a simple idea:

> **Finding an error is only the first step. Understanding why it happened and how to fix it is what makes debugging easier.**

By combining program analysis with NLP, this project attempts to make technical debugging information more accessible and understandable.

---

## 📌 Status

🚧 **Currently in development**

The core repository analysis, Python parsing, error detection, NLP-based error matching, explanation generation, and suggested-fix pipeline have been implemented. The Streamlit interface is being developed as the final application layer.
