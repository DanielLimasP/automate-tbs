#! python3 
# pdf_merge.py - Combine several pdfs in cwd into a single file

import PyPDF2
from pathlib import Path
import os

cwd = Path.cwd() / 'pdfs'

# List and sort the names
pdf_files = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)

pdf_files.sort()

# Create a pdf writer
pdf_writer = PyPDF2.PdfFileWriter()

# Loop through all the pdf files
for filename in pdf_files:
    pdf_file = open(cwd / filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Loop through all the pages (excluding the first) and add them
    for page in range(1, pdf_reader.numPages):
        page = pdf_reader.getPage(page)
        pdf_writer.addPage()

# Save th resulting pdf
pdf_output = open(cwd / 'allminutes.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
