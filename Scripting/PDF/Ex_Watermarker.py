import PyPDF2

def pdf_watermarker(input_pdf, output_pdf, watermark_pdf):
  watermark_reader = PyPDF2.PdfFileReader(watermark_pdf)
  watermark = watermark_reader.getPage(0)

  input_reader = PyPDF2.PdfFileReader(input_pdf)
  output_writer = PyPDF2.PdfFileWriter()

  for i in range(input_reader.numPages):
    page = input_reader.getPage(i)
    page.mergePage(watermark)
    output_writer.addPage(page)

  with open('watermarked.pdf', mode='wb') as out:
    output_writer.write(out)

pdf_watermarker('merged.pdf', 'watermarked.pdf', 'wtr.pdf')

# ALTERNATIVE
template = PyPDF2.PdfFileReader(open('merged.pdf', 'rb'))
watermark2 = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i) 
  page.mergePage(watermark2.getPage(0))
  output.addPage(page)

with open('watermarked.pdf', 'wb') as file:
  output.write(file)
