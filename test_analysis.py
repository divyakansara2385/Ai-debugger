from analyzer.repository import clone_repository, get_source_files
from analyzer.analyzer import analyze_file


repo_url = input("Enter GitHub repository URL: ")

repo_path = clone_repository(repo_url)

files = get_source_files(repo_path)

print("\nSource files found:")
print("-------------------")

for file in files:
    print(file["language"], "→", file["path"])


print("\n\n========== ANALYSIS ==========")

for file in files:

    if file["language"] != "Python":
        continue

    print("\nAnalyzing:", file["path"])

    result = analyze_file(file["path"])

    if not result["errors"]:
        print("No errors detected.")
        continue

    for error in result["errors"]:

        print("\nType:", error["type"])

        if "variable" in error:
            print("Variable:", error["variable"])

        print("Line:", error["line"])

        if "explanation" in error:
            print("Explanation:", error["explanation"])

        if "suggested_fix" in error:
            print("Suggested Fix:", error["suggested_fix"])

        if "similarity" in error:
            print(
                "NLP Similarity:",
                round(error["similarity"], 2)
            )