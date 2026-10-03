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

if not test_folder.is_dir():
    raise SystemExit(f"Folder not found: {test_folder}")

moved_count = 0
renamed_count = 0

for item in test_folder.iterdir():
    if not item.is_file():
        continue

    extension = item.suffix.lower()
    category = category_for(extension)

    destination_folder = test_folder / category
    destination_folder.mkdir(exist_ok=True)
    destination = destination_folder / item.name

    number = 2
    while destination.exists():
        destination = destination_folder / f"{item.stem}_{number}{item.suffix}"
        number += 1

    if number > 2:
        renamed_count += 1

    item.rename(destination)
    moved_count += 1
    print("Moved:", item.name, "->", destination)

print("Finished. Moved:", moved_count, "Renamed:", renamed_count)
