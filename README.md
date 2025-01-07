# Python Keylogger

## Overview
This is a Python-based keylogger for **educational purposes only**. It demonstrates how keylogging works and sends logged keys via email at regular intervals.

## Features
- Logs every keypress, including special keys.
- Sends email reports with logs at a specified interval.

## Requirements
- Python 3.x
- `pynput` library: Install with `pip install pynput`

## Usage
1. Replace `MAIL` and `APP_PASSWORD` in `sam.py` with your Gmail address and app password.
2. Run the main script:
   ```bash
   sam.py


## Converting Python Scripts to Executables
If you want to use the Python scripts as standalone executables on Windows, follow these steps:

### Prerequisites
- Install Python 3.x
- Install `pip` if not already installed.
- Install PyInstaller using the command:
  ```bash
  pip install pyinstaller
Steps
Place all Python files (sample_key.py and sam.py) in the same directory.
Open a terminal or command prompt in the directory containing the files.
Run the following commands to create executables:
For sample_key.py:
pyinstaller --onefile sample_key.py
For main.py:
pyinstaller --onefile main.py
The executables will be generated in the dist folder.

Optional
To hide the console window when running the executables (e.g., for the keylogger), use the --noconsole flag:
pyinstaller --onefile --noconsole sam.py
If dependencies are missing, include them explicitly with the --add-data option:
pyinstaller --onefile --add-data "sam.py;." main.py
Testing
After conversion, run the .exe files to ensure all functionalities work as expected.
Disclaimer

All scripts and tools in this repository are for educational purposes only. The misuse of these tools can result in serious legal consequences. Always use them responsibly and only on systems you own or have explicit permission to test.
Contributions

Contributions to improve this repository are welcome! Please ensure your additions align with the educational and ethical focus of this project.
License

This repository is licensed under the MIT License. See the LICENSE file for more details.

---

Let me know if you’d like further refinements!
