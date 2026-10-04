from pathlib import Path

def category_for(file_extension):
    if file_extension in {".jpg", ".jpeg", ".png"}:
        return "Images"
    elif file_extension in {".txt", ".pdf", ".docx"}:
        return "Documents"
    elif file_extension in {".mp4", ".mov", ".avi", ".webm", ".wmv"}:
        return "Videos"
    elif file_extension in {".wav", ".aif", ".aiff", ".flac", ".m4a", ".mp3", ".aac", ".oga", ".wma"}:
        return "Audio"
    else:
        return "Other"

folder_text = input("Enter the folder to organize: ").strip()

if not folder_text:
    raise SystemExit("No folder entered.")

source_folder = Path(folder_text)

if not source_folder.is_dir():
    raise SystemExit(f"Folder not found: {source_folder}")

print("Selected folder:", source_folder.resolve())
print("\nPreview:")
planned_moves = []
reserved_destinations = set()

for item in sorted(source_folder.iterdir()):
    if not item.is_file():
        continue

    category = category_for(item.suffix.lower())
    destination_folder = source_folder / category
    destination = destination_folder / item.name

    number = 2
    while destination.exists() or destination in reserved_destinations:
        destination = destination_folder / f"{item.stem}_{number}{item.suffix}"
        number += 1

    planned_moves.append((item, destination))
    reserved_destinations.add(destination)
    print(f"{item.name} -> {destination.relative_to(source_folder)}")

print("Files to organize:", len(planned_moves))

if len(planned_moves) == 0:
    raise SystemExit("No files to organize.")

confirmation = input("Type ORGANIZE to move its files:").strip()
if confirmation != "ORGANIZE":
    raise SystemExit("Cancelled. No files moved.")

moved_count = 0
renamed_count = 0

for item, destination in planned_moves:
    destination.parent.mkdir(exist_ok=True)

    if destination.exists():
        raise SystemExit(f"Destination appeared after preview: {destination}")

    item.rename(destination)
    moved_count += 1

    if item.name != destination.name:
        renamed_count += 1

    print("Moved:", item.name, "->", destination)

print("Finished. Moved:", moved_count, "Renamed:", renamed_count)
