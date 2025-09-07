# Simple QR Code Generator

A simple Python application that generates QR codes from URLs and saves them as images.

## Features

- Generate QR codes from any URL
- Save QR codes as PNG images in the same directory
- Automatic URL validation and formatting
- Auto-generated timestamps for filenames
- Command-line and interactive modes

## Installation

1. Install the required dependencies:
```bash
pip install qrcode[pil] Pillow
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode
Simply run the script and follow the prompts:
```bash
python qr_generator.py
```

### Command Line Mode
Provide the URL as a command line argument:
```bash
python qr_generator.py "https://www.google.com"
```

You can also specify a custom filename:
```bash
python qr_generator.py "https://www.google.com" "google_qr"
```

## Examples

```bash
# Interactive mode
python qr_generator.py

# Generate QR code for Google
python qr_generator.py "https://www.google.com"

# Generate QR code with custom filename
python qr_generator.py "https://github.com" "github_qr"

# URLs without protocol are automatically prefixed with https://
python qr_generator.py "stackoverflow.com"
```

## Output

The generated QR code images are saved in the same directory as the script with the following naming convention:
- Auto-generated: `qr_code_YYYYMMDD_HHMMSS.png`
- Custom filename: `your_filename.png`

## Requirements

- Python 3.6+
- qrcode library with PIL support
- Pillow (PIL)
