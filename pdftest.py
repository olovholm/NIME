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
MACROSTRING = re.compile('(abstract)([\w\s]*)(keywords)([\w\s]*)(INTRODUCTION)', flags=re.MULTILINE | re.IGNORECASE)
CASESTRING = re.compile('(ABSTRACT)(.*)(keywords)(.*)(INTRODUCTION)', flags=re.MULTILINE)

dir_path = "nime_archive/web/"
pdf_array = []

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
  def __init__(self, pdf, infile):
    self.infile = infile
    self.pdf = pdf
    self.meta = pdf.getDocumentInfo()
    self.pagenum = pdf.getNumPages()
    self.loadMeta()
    self.pages = []
    self.found = False
    for i in range(0,self.pagenum):
      temp_page = self.pdf.getPage(i)
      self.pages.append(PdfPage(temp_page))

    self.extractor()
  
          
  def loadMeta(self):
    try:
      self.producer = self.meta['/Producer']
      print "filename: %s \t \t producer = %s" % (infile, self.producer)
    except Exception as e:
      #print "error extracting DocumentInfo from file:%s, %s" % (workfile ,e)
      print e

    try:
      self.creator = self.meta['/Creator']
      print "filename: %s \t \t creator = %s" % (infile, self.creator)
    except Exception as e:
      #print "error extracting Creator from file:%s, %s" % (workfile ,e)
      print e
        
    try:
      self.title = self.meta['/Title']
      print "filename: %s \t \t title = %s" % (infile, self.title)
    except Exception as e:
      #print "error extracting Title from file:%s, %s" % (workfile ,e)
      print e
          
      
      
      
      
  def extractor(self):
    for i in range(0,self.pagenum):
      val01 = self.extract_01(self.pages[i].returnText())
      val02 = self.extract_02(self.pages[i].returnText())
      val03 = self.extract_03(self.pages[i].returnText())
      if val01 or val02 or val03:
        print "found"
        self.found = True
      else:
        print "could not find"
        
          
#
# TODO: From this point and onward, the idea is to have various extraction methods controlled by a controller which tests if the pattern
# gets recognized and alters flow to other elements if that is not so 
#
 
 
  #Runs through the pdf-files checks the strings as they are
  def extract_01(self,text):
    splits = re.findall(SEARCHSTRING, text)
    if len(splits) > 0:
      print "Found %s " % splits
      print found[folder]
      return True
    else:
      return False
      
  #Runs through the pdf-files, but looks at the text in an attempt to see whether they are of another charset. 
  def extract_02(self,text):
    text = text.encode("utf-8")
    splits = re.findall(CASESTRING, text)
    if len(splits) > 0:
      print "Found %s " % splits
      print found[folder]
      return True
    else:
      return False
      
  def extract_03(self,text):
    text = text.encode("utf-8")
    splits = re.findall(MACROSTRING, text)
    if len(splits) > 0:
      print "Found %s " % splits
      print found[folder]
      return True
    else:
      return False
      
    
      





for folder in os.listdir(dir_path):
  if os.path.isdir(dir_path+folder) == True:
    for infile in os.listdir(dir_path+folder):
      #print infile
      if infile.endswith(".pdf"):
        workfile = dir_path + folder + "/"+ infile
        try:
          input1 = PdfFileReader(file(workfile, "rb"))
          pdf = PdfDoc(input1, infile)
          pdf_array.append(pdf)
        except Exception as e:
          print "Could not open file: %s, %s" % (workfile,e)
          break

          


