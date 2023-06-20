import PyPDF2

template = PyPDF2.PdfFileReader(open('./scripting_with_python/working_pdf/super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('./scripting_with_python/working_pdf/wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('./scripting_with_python/working_pdf/water_marked.pdf', 'wb') as file:
        output.write(file)