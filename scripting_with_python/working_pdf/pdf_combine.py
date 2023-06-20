import PyPDF2, sys

inputs = sys.argv[1:]

def pdf_combiner(list_input):
    merger = PyPDF2.PdfFileMerger()
    for pdf in list_input:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)