from analyzer.repository import clone_repository, get_source_files

repo_url = input("Enter GitHub repository URL: ")

repo_path = clone_repository(repo_url)

files = get_source_files(repo_path)

print("\nSource files found:\n")

for file in files:
    print(file["language"], "→", file["path"])