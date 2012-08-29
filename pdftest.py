#!/usr/bin/python
#-*- coding: utf-8


#
# This script runs through the pdf files in the nime2012 folder and tries to extact text from the pdf files. Text is written to screen.
# Should implement a limitation on how much of the files which are printed. Should also look for formatting. 
#
# Alternative python pdf libraries: pyPdf, PDFMiner
# Tip from stackoverflow: https://code.google.com/p/pdfssa4met/


import os
import re
from pyPdf import PdfFileReader
import subprocess

abstract_word = "abstract"
introduction_word = {"intro", "introduction"}



dir_path = "nime_archive/web/2008/"
for infile in os.listdir(dir_path):
    if infile.endswith(".pdf"):
        workfile = dir_path + infile
        input1 = PdfFileReader(file(workfile, "rb"))
        #print "!!--- ARTICLE START ---!!"
        #try:
            #print "title = %s " % (input1.getDocumentInfo())
        #except Exception as e:
           # print e
        pagenum = (input1.getNumPages())
        for i in range(0,pagenum):
            #print "!!--- PAGE START: %i ---!!" % i
            fp = input1.getPage(i)
            text = fp.extractText().encode("UTF-8")
            prog = re.compile('(abstract)(.*)(keywords)(.*)(.*INTRODUCTION.*)', flags=re.MULTILINE | re.IGNORECASE)
            splits = re.findall(prog, text)
            if len(splits) > 0:
               # print "Found %s " % splits
               print "Found %s" % infile
            else:
                if i == 0:
                    print "Found nothing: %s" % infile
            
    
        
