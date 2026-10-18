from pathlib import Path

#map file extensions to categories 
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

def available_destination(item, destination_folder, reserved_destinations):
    destination = destination_folder / item.name
    number = 2

    while destination.exists() or destination in reserved_destinations:
        destination = destination_folder / f"{item.stem}_{number}{item.suffix}"
        number += 1

    return destination

folder_text = input("Enter the folder to organize: ").strip()

if not folder_text:
    raise SystemExit("No folder entered.")

source_folder = Path(folder_text)

#If the folder doesn't exist, exit the program with an error message
if not source_folder.is_dir():
    raise SystemExit(f"Folder not found: {source_folder}")

print("Selected folder:", source_folder.resolve())
print("\nPreview:")
planned_moves = []
reserved_destinations = set()
category_counts = {}

for item in sorted(source_folder.iterdir()):
    if not item.is_file():
        continue

    category = category_for(item.suffix.lower())
    category_counts[category] = category_counts.get(category, 0) + 1
    destination_folder = source_folder / category

    destination = available_destination(item, destination_folder, reserved_destinations)

    planned_moves.append((item, destination))
    reserved_destinations.add(destination)
    print(f"{item.name} -> {destination.relative_to(source_folder)}")

print("\nFiles by category:")

for category, count in sorted(category_counts.items()):
    print(f" {category}: {count}")
print("Files to organize:", len(planned_moves))
for category, count in category_counts.items():
    print(f"{category}: {count}")

if len(planned_moves) == 0:
    raise SystemExit("No files to organize.")

confirmation = input("Type ORGANIZE to move its files:").strip()
if confirmation != "ORGANIZE":
    raise SystemExit("Cancelled. No files moved.")

moved_count = 0
renamed_count = 0
failed_count = 0

for item, destination in planned_moves:
    try:
        destination.parent.mkdir(exist_ok=True)

        if destination.exists():
            print(f"Skipped: Destination already exists: {destination}")
            failed_count += 1
            continue

        item.rename(destination)

    except OSError as error:
        failed_count += 1
        print(f"Failed to move {item.name}: {error}")
        continue
    
    moved_count += 1

    if item.name != destination.name:
        renamed_count += 1

    print("Moved:", item.name, "->", destination)

print("\nOrganization complete!")
print("Files moved:", moved_count)
print("Files renamed:", renamed_count)
print("Files that failed to move:", failed_count)
