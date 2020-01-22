import PyPDF2

with open('dummy.pdf', 'rb') as file:
  reader = PyPDF2.PdfFileReader(file) # we need to read the file as binary
  # print(reader.numPages)
  # print(reader.getPage(0)) # get first page
  page = reader.getPage(0)
  print(page.rotateCounterClockwise(90))
  writer = PyPDF2.PdfFileWriter()
  writer.addPage(page)
  with open('tilt.pdf', 'wb') as new_file:
    writer.write(new_file)

