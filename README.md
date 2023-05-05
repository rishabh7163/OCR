# PDF_OCR

This is a simple Python project that reads a pdf file and prints out all the words from that file.

## Installation

To use this project, you need to have Python 3 installed on your computer. You can download Python 3 from the official website: https://www.python.org/downloads/


## Usage

To run the project, you can simply run the following command:

```
python ocr.py
```
Replace "example.pdf" with your pdf file name.
```
pdf_file = fitz.open('path_to_file example.pdf')

The program will then read the file and print out all the words along with their frequency.


## Process:
  a) Opens the file 
  b) Creates a PDF reader object 
  c) Gets the number of pages 
  d) Loops through each page 
  e) Extracts the text from each page 
  f) Prints the text to the console. You can modify the script to extract specific information from the PDF file instead of just printing the text.



## Contributing

This project is open for contributions. If you have any ideas or suggestions, feel free to open an issue or submit a pull request.



## License

This project is licensed under the MIT License. See the LICENSE file for more information.

