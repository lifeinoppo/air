# coding: utf-8
import csv, os, time
from pyPdf import PdfFileWriter, PdfFileReader

#getting current Merge2PDF.py derectory.
#make directories for source file and merged file
pyDt = os.getcwd()
sourceDt = pyDt + '/source'
mergedDt = pyDt + '/merged'

#open pages.csv and read page numbers.
lst = [2,3]


#manipulate before.pdf and after.pdf
#note: for runing in company computer, renmae before and after file with
#extension .xls for some reason we all know.
input1 = PdfFileReader(file(sourceDt+"/before.pdf", "rb"))
input2 = PdfFileReader(file(sourceDt+"/after.pdf", "rb"))
output = PdfFileWriter()

for i in lst:
	output.addPage(input1.getPage(i-1))
for i in lst:
        output.addPage(input2.getPage(i-1))

#get time in format year-mon-day_hour-minute-sec
localtime = time.strftime('%Y-%m-%d_%X',time.localtime(time.time()))
localtime = localtime.replace(':','-')

outputname = mergedDt + "/Merged_" + localtime + ".pdf"
outputStream = file(outputname,"wb")
output.write(outputStream)
outputStream.close()

print "It's done!"
