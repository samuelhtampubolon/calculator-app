# Calculator App

Simple desktop calculator built with Python + Tkinter, packaged as a Windows `.exe` with PyInstaller.

## Features
- Basic ops: `+ - × ÷ % ± . C ⌫ =`
- Keyboard support: `0-9 + - * / % ( )`, `Enter` = equals, `Backspace` = delete, `Esc` = clear
- Dark theme GUI
- Error handling (e.g. divide by zero)

## Run from source
```bash
python calculator.py
```

## Run exe
Double-click `dist/Calculator.exe` (no Python needed).

## Build exe
```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name Calculator calculator.py
```
Output: `dist/Calculator.exe`
