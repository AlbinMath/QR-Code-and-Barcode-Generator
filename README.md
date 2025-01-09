# QR Code and Barcode Generator

A Python-based application for generating QR codes and barcodes using a graphical user interface (GUI) built with `tkinter`. This tool allows users to create and save QR codes or barcodes to a specified directory.

---

## Features

- Generate **QR Codes** from text or URLs.
- Generate **Barcodes** from text.
- Save generated codes as images (`.png` format).
- User-friendly GUI with options to specify:
  - Input text or URL.
  - Output file name and save location.
  - QR code size.

---

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.6 or higher
- `pip` (Python package manager)

### Install Required Libraries
Run the following commands to install the necessary Python libraries:


pip install qrcode[pil]
pip install python-barcode Pillow


## Usage
1. Clone the repository:

git clone https://github.com/AlbinMath/QR-Code-and-Barcode-Generator.git

cd QR-Code-and-Barcode-Generator

2. Run the script:

python app.py

3. Use the GUI to:

Select code type (QR Code or Barcode).
Enter the text or URL to encode.
Specify a save location and file name.
Set the size for QR codes (1–40).

## GUI Layout
Code Type: Dropdown to choose between QR Code or Barcode.
Text/URL: Input field for the content to encode.
Save Location: Field and "Browse" button to select the output directory.
File Name: Input field to specify the output file name.
QR Code Size: Optional size input for QR codes.
Generate Button: Generates the QR Code or Barcode.
Clear All Button: Clears all input fields.

Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

Author:

Name : Albin Mathew - [GitHub Profile](https://github.com/AlbinMath/)
