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
   python main.py
