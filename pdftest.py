#!/usr/bin/python

#
# This script runs through the pdf files in the nime2012 folder and tries to extact text from the pdf files. Text is written to screen.
# Should implement a limitation on how much of the files which are printed. Should also look for formatting. 
#
# Alternative python pdf libraries: pyPdf, PDFMiner
# Tip from stackoverflow: https://code.google.com/p/pdfssa4met/


import os
from pyPdf import PdfFileReader
import subprocess

abstract_word = "abstract"
introduction_word = {"intro", "introduction"}


dir_path = "testfiles/"
for infile in os.listdir(dir_path):
    workfile = dir_path + infile
    #subprocess.call(['pdftotext', workfile, 'output'])
    input1 = PdfFileReader(file(workfile, "rb"))
    print "!!--- ARTICLE START ---!!"
    print "title = %s " % (input1.getNumPages)
    pagenum = (input1.getNumPages())
    for i in range(0,pagenum):
        print "!!--- PAGE START: %i ---!!" % i
        fp = input1.getPage(0)
        print fp.extractText()
