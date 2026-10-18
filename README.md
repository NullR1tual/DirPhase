<div align="center">
  <img src="assets/dirphase-github-logo.png" alt="DirPhase — file organization utility" width="720">

  <p><strong>Put your files in their place.</strong></p>
  <p>A lightweight Python command-line utility that organizes files into folders by type, without moving anything until you approve the plan.</p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python 3.x">
    <img src="https://img.shields.io/badge/interface-CLI-0C939D" alt="Command-line interface">
    <img src="https://img.shields.io/badge/license-PolyForm%20Noncommercial%201.0.0-5B6473" alt="PolyForm Noncommercial 1.0.0">
  </p>
</div>

---

## Overview

A cluttered Downloads folder shouldn't take an afternoon to clean up.

**DirPhase** helps organize the files in a selected folder by moving them into category-based subfolders. Before anything changes, it shows you exactly where each file is headed and waits for your confirmation. If a filename already exists at the destination, DirPhase chooses an available numbered name instead of overwriting it.

DirPhase is currently a **command-line Python script**, not a packaged desktop app. It uses only the Python standard library.

## Features

- **Automatic categorization** - sorts files into `Images`, `Documents`, `Videos`, `Audio`, or `Other` based on extension.
- **Move preview** - lists every proposed move before changing files.
- **Explicit confirmation** - requires you to type `ORGANIZE` to proceed; anything else cancels.
- **Duplicate filename handling** - uses names like `photo_2.jpg` when a destination filename is already taken.
- **Case-insensitive extension matching** - recognizes `.JPG` the same way as `.jpg`.
- **Simple summary** - reports the number of files moved and renamed.
- **No third-party dependencies** - built with Python's `pathlib` module.

## Before and after

For example, a folder containing these files:

```text
Downloads/
├── photo.jpg
├── notes.txt
├── presentation.mp4
└── music.mp3
```

Becomes:

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── notes.txt
├── Videos/
│   └── presentation.mp4
└── Audio/
    └── music.mp3
```

Only files directly inside the selected folder are considered. Existing subfolders are left alone.

## Requirements

- Python 3 installed and accessible from your terminal.
- A folder you have permission to read from and write to.

There is **nothing to install with `pip`**.

## Getting started

### 1. Get the code

Clone the repository:

```bash
git clone https://github.com/NullR1tual/DirPhase.git
cd DirPhase
```

Or select **Code → Download ZIP** on GitHub and extract it.

### 2. Run DirPhase

From the repository folder, run:

```bash
python organizer.py
```

If your computer uses a different Python command, try `python3 organizer.py` (commonly on macOS/Linux) or `py organizer.py` (Windows with the Python launcher).

### 3. Select a folder

When prompted, enter the path to the folder you want to organize:

```text
Enter the folder to organize: C:\Users\YourName\Downloads
```

The folder must already exist. On Windows, paste the path **without surrounding quotation marks**, even if it contains spaces.

### 4. Review and confirm

DirPhase prints its proposed changes first. A session might look like this:

```text
Selected folder: C:\Users\YourName\Downloads

Preview:
music.mp3 -> Audio\music.mp3
notes.txt -> Documents\notes.txt
photo.jpg -> Images\photo.jpg
presentation.mp4 -> Videos\presentation.mp4
Files to organize: 4
Type ORGANIZE to move its files: ORGANIZE
Moved: music.mp3 -> C:\Users\YourName\Downloads\Audio\music.mp3
Moved: notes.txt -> C:\Users\YourName\Downloads\Documents\notes.txt
Moved: photo.jpg -> C:\Users\YourName\Downloads\Images\photo.jpg
Moved: presentation.mp4 -> C:\Users\YourName\Downloads\Videos\presentation.mp4
Finished. Moved: 4 Renamed: 0
```

**Nothing moves unless you type `ORGANIZE` exactly.** Press Enter without typing it—or type anything else—to cancel.

## Supported file types

| Destination folder | Recognized extensions |
| --- | --- |
| **Images** | `.jpg`, `.jpeg`, `.png` |
| **Documents** | `.txt`, `.pdf`, `.docx` |
| **Videos** | `.mp4`, `.mov`, `.avi`, `.webm`, `.wmv` |
| **Audio** | `.wav`, `.aif`, `.aiff`, `.flac`, `.m4a`, `.mp3`, `.aac`, `.oga`, `.wma` |
| **Other** | Any extension not listed above, including files without an extension |

Categories are currently defined in `category_for()` inside [`organizer.py`](organizer.py). More formats may be added in future versions.

## File safety and limitations

> [!CAUTION]
> **DirPhase moves files; it does not copy them.** Test it on a folder containing nonessential files first, and keep backups of anything important. There is currently **no undo or automatic rollback**.

- **Preview first:** Proposed destination paths are shown before you confirm.
- **Avoids overwriting:** If a name already exists in its destination category, DirPhase tries a numbered filename such as `photo_2.jpg`.
- **Nonrecursive:** Only files in the top level of your selected folder are processed. Subdirectories are skipped.
- **No background monitoring:** DirPhase runs once for the folder you select; it does not continually watch it for new files.
- **No GUI yet:** DirPhase currently runs in a terminal.
- **Partial moves are possible:** If an error occurs after moving has started, files moved earlier in the run are not automatically restored.

## Roadmap

DirPhase is an actively evolving learning project. These are possible next steps, **not features available today**:

- [x] Categorize common file types
- [x] Preview proposed moves
- [x] Require confirmation before moving
- [x] Handle duplicate destination filenames
- [ ] Expand supported extensions and allow custom categories
- [ ] Add a dedicated preview-only option
- [ ] Add logging and an undo/rollback workflow
- [ ] Introduce automated tests
- [ ] Build a desktop GUI
- [ ] Package standalone releases

## Feedback and contributions

Found a bug or have an idea? [Open an issue](https://github.com/NullR1tual/DirPhase/issues) with a description of what happened, your operating system and Python version, and steps to reproduce the issue if possible.

Please discuss substantial changes in an issue before opening a pull request. This project is **source-available rather than OSI-approved open source**, and its license governs permitted uses and distribution.

## License

DirPhase is made available under the **[PolyForm Noncommercial License 1.0.0](LICENSE.md)**. See the [copyright notice](NOTICE).

The license permits uses within its defined scope, including noncommercial use and certain organizational exceptions. Uses outside those permissions—such as commercial exploitation not otherwise permitted by the license—require separate authorization from the copyright holder.

For commercial licensing inquiries, contact the maintainer through the [GitHub profile](https://github.com/NullR1tual). The full [license text](LICENSE.md) controls if it differs from this summary.

---

<div align="center">
  <sub>Built with Python · Maintained by <a href="https://github.com/NullR1tual">NullR1tual</a></sub>
</div>
