from pathlib import Path

def category_for(file_extension):
    if file_extension in {".jpg", ".jpeg", ".png"}:
        return "Images"
    elif file_extension in {".txt", ".pdf", ".docx"}:
        return "Documents"
    else:
        return "Other"

folder_text = input("Enter the folder to organize: ").strip()

if not folder_text:
    raise SystemExit("No folder entered.")

source_folder = Path(folder_text)

if not source_folder.is_dir():
    raise SystemExit(f"Folder not found: {source_folder}")

print("Selected folder:", source_folder.resolve())

confirmation = input("Type ORGANIZE to move its files:").strip()
if confirmation != "ORGANIZE":
    raise SystemExit("Cancelled. No files moved.")

moved_count = 0
renamed_count = 0

for item in source_folder.iterdir():
    if not item.is_file():
        continue

    extension = item.suffix.lower()
    category = category_for(extension)

    destination_folder = source_folder / category
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
