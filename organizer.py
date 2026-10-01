from pathlib import Path

def category_for(file_extension):
    if file_extension in {".jpg", ".jpeg", ".png"}:
        return "Images"
    elif file_extension in {".txt", ".pdf", ".docx"}:
        return "Documents"
    else:
        return "Other"

project_folder = Path(__file__).parent
test_folder = project_folder / "test_files"

moved_count = 0
skipped_count = 0

for item in test_folder.iterdir():
    if not item.is_file():
        continue

    extension = item.suffix.lower()
    category = category_for(extension)

    destination_folder = test_folder / category
    destination_folder.mkdir(exist_ok=True)
    destination = destination_folder / item.name

    if destination.exists():
        skipped_count += 1
        print("Skipped (already exists):", destination)
        continue

    item.rename(destination)
    moved_count += 1
    print("Moved:", item.name, "->", destination)

print("Finished. Moved:", moved_count, "Skipped:", skipped_count)
