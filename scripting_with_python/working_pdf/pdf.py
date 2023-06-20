import PyPDF2

with open('./scripting_with_python/working_pdf/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./scripting_with_python/working_pdf/tilt.pdf', 'wb') as file1:
        writer.write(file1)