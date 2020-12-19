import PyPDF2
import os

pdf_file_obj = open()
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
pdf_reader.numPages
page_obj = pdf_reader.getPage(0)
page_obj.extractText()
pdf_file_obj.close()