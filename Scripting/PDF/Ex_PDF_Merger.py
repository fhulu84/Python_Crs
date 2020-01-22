import sys
from PyPDF2 import PdfFileMerger

files = sys.argv[1:]

def pdf_merger(files):
  merger = PdfFileMerger()

  for file in files:
    merger.append(file)
  
  with open('merged.pdf', mode='wb') as merged:
    merger.write(merged)

pdf_merger(files)
