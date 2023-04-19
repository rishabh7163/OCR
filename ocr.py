import fitz

# Open the PDF file
pdf_file = fitz.open('path_to_file example.pdf')

# Get the number of pages in the PDF file
num_pages = pdf_file.page_count

# Loop through each page in the PDF file
for page_num in range(num_pages):
    # Get the current page object
    page = pdf_file[page_num]

    # Extract the text from the current page
    text = page.get_text()

    # Do something with the extracted text
    print(text)

# Close the PDF file
pdf_file.close()
