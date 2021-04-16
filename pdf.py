import PyPDF2

#grab super.pdf what we will process and wtr. pdf and open up
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

#write my output and combine the above files
output = PyPDF2.PdfFileWriter()

