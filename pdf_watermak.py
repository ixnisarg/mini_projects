import PyPDF2
import sys
input = sys.argv[1]

template = PyPDF2.PdfFileReader(open(input,'rb'))
watermark =PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked.pdf','rb') as file:
        output.write(file)
