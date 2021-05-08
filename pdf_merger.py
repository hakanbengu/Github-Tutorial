import os
from PyPDF2 import PdfFileMerger

source_dir = os.getcwd()

merger = PdfFileMerger()

for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(item)

if not os.path.exists('pdfmerger'):
    os.makedirs('pdfmerger')

merger.write('./pdfmerger/Lecture Complete.pdf')       
merger.close()