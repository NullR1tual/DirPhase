from pathlib import Path

project_folder = Path(__file__).parent
test_folder = project_folder / "test_files"

for item in test_folder.iterdir():
    if not item.is_file():
        continue

    extension = item.suffix.lower()

    if extension in {".jpg", ".jpeg", ".png"}:
        category = "Images"
    elif extension in {".txt", ".pdf", ".docx"}:
        category = "Documents"
    else:
        category = "Other"

    destination_folder = test_folder / category
    destination = destination_folder / item.name
    print(item, "->", destination)