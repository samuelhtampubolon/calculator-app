# Calculator App / Aplikasi Kalkulator

Simple desktop calculator built with Python + Tkinter, packaged as a Windows `.exe` with PyInstaller.
Kalkulator desktop sederhana dengan Python + Tkinter, dikemas sebagai `.exe` Windows dengan PyInstaller.

Bilingual: English / Bahasa Indonesia — switch with EN / ID buttons at the top.
Dwibahasa: Inggris / Bahasa Indonesia — ganti dengan tombol EN / ID di atas.

## Features / Fitur
- Basic ops / Operasi dasar: `+ - × ÷ % ± . C ⌫ =`
- Keyboard support / Dukungan keyboard: `0-9 + - * / % ( )`, `Enter` = equals / sama dengan, `Backspace` = delete / hapus, `Esc` = clear / bersihkan
- Dark theme GUI / Tampilan gelap
- Bilingual UI: title + errors / UI dwibahasa: judul + pesan kesalahan
  - EN: `Calculator`, `Error`, `Can't divide by 0`
  - ID: `Kalkulator`, `Kesalahan`, `Tidak bisa dibagi 0`
- Error handling / Penanganan kesalahan (e.g. divide by zero / contoh pembagian nol)

## Run from source / Jalankan dari source
```bash
python calculator.py
```

## Run exe / Jalankan exe
Double-click `dist/Calculator.exe` (no Python needed).
Klik dua kali `dist/Calculator.exe` (tanpa Python).

## Build exe / Bangun exe
```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name Calculator calculator.py
```
Output: `dist/Calculator.exe`
