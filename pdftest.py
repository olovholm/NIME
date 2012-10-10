#!/usr/bin/python
#-*- coding: utf-8



# This script runs through the pdf files in the nime2012 folder and tries to extact text from the pdf files. Text is written to screen.
# Should implement a limitation on how much of the files which are printed. Should also look for formatting.
#
# Alternative python pdf libraries: pyPdf, PDFMiner
# Tip from stackoverflow: https://code.google.com/p/pdfssa4met/

import os
import re
from pyPdf import PdfFileReader
import subprocess

abstract_word = "abstract"
introduction_word = {"intro", "introduction"}
SEARCHSTRING = re.compile('(abstract)(.*)(keywords)(.*)(INTRODUCTION)', flags=re.MULTILINE | re.IGNORECASE)

dir_path = "nime_archive/web/"
found = {}
found_nothing = {}

#
# Class PdfPage - contains a PdfPage, extracts text and return this upon request
#
class PdfPage:
  def __init__(self, page):
    self.text = page.extractText()

  def returnText(self):
    return self.text


#
# PdfDoc - contains a PdfDoc, metadata and controls the flow of the extraction
#

class PdfDoc:
  #Instanciates the PdfDoc object. Reads the file and sets the producer-variable
  def __init__(self, pdf):
    self.pdf = pdf
    self.meta = pdf.getDocumentInfo()
    self.pagenum = pdf.getNumPages()
    self.loadMeta()
    self.pages = []
    for i in range(0,self.pagenum):
      temp_page = pdf.getPage(i)
      self.pages.append(PdfPage(temp_page))
      print self.pages[i].returnText()
        
  def loadMeta(self):
    try:
      self.producer = self.meta['/Producer']
      print "filename: %s \t \t producer = %s" % (infile, self.producer)
    except Exception as e:
      #print "error extracting DocumentInfo from file:%s, %s" % (workfile ,e)
      print " "

    try:
      self.creator = self.meta['/Creator']
      print "filename: %s \t \t creator = %s" % (infile, self.creator)
    except Exception as e:
      #print "error extracting Creator from file:%s, %s" % (workfile ,e)
      print " "
        
    try:
      self.title = self.meta['/Title']
      print "filename: %s \t \t title = %s" % (infile, self.title)
    except Exception as e:
      #print "error extracting Title from file:%s, %s" % (workfile ,e)
      print " "
          
    try:
      self.title = self.meta['/CreationDate']
      print "filename: %s \t \t CreationDate = %s" % (infile, self.creationdate)
    except Exception as e:
      #print "error extracting CreationDate from file:%s, %s" % (workfile ,e)
      print " "
        
    try:
      self.title = self.meta['/ModDate']
      print "filename: %s \t \t ModDate = %s" % (infile, self.moddate)
    except Exception as e:
      #print "error extracting ModDate from file:%s, %s" % (workfile ,e)
      print " " 
        
          
#
# TODO: From this point and onward, the idea is to have various extraction methods controlled by a controller which tests if the pattern
# gets recognized and alters flow to other elements if that is not so 
#
          

  def extract_01(self,text):
    splits = re.findall(SEARCHSTRING, text)
    if len(splits) > 0:
      # print "Found %s " % splits
      print found[folder]
      return True
    else:
      if i == 0:
          return False
      
      





for folder in os.listdir(dir_path):
  found[folder] = 0
  found_nothing[folder] = 0
  if os.path.isdir(dir_path+folder) == True:
    for infile in os.listdir(dir_path+folder):
      #print infile
      if infile.endswith(".pdf"):
        workfile = dir_path + folder + "/"+ infile
        try:
          input1 = PdfFileReader(file(workfile, "rb"))
          pdf = PdfDoc(input1)
        except Exception as e:
          print "Could not open file: %s, %s" % (workfile,e)
          break

          


