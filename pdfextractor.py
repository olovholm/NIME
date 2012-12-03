#!/usr/bin/python
#-*- coding: utf-8



# This script runs through the pdf files in the nime2012 folder and tries to extact text from the pdf files. Text is written to screen.
# Should implement a limitation on how much of the files which are printed. Should also look for formatting.
#
# Alternative python pdf libraries: pyPdf, PDFMiner
# Tip from stackoverflow: https://code.google.com/p/pdfssa4met/

import os
import re
import subprocess
import pprint
from lxml import etree

SEARCHSTRING = re.compile('abstract(.*)keywords(.*)introduction', flags=re.MULTILINE | re.IGNORECASE | re.DOTALL)

dir_path = "nime_archive/web/"
documents = []


#
# PdfDoc - contains a PdfDoc, metadata and controls the flow of the extraction
#

class PdfDoc:
  #Instanciates the PdfDoc object. Reads the file and sets the producer-variable
  def __init__(self, filename, text):
    self.filename = filename
    self.text = text
    self.extracted_abstract = False
    self.extracted_keywords = False
    self.abstract = ""
    self.keywords = ""
    self.extractor()
    self.clean_keywords()
    self.remove_difficult_chars()

  def extractor(self):
    val = self.extract(self.text)
 
 
  #Runs through the pdf-files checks the strings as they are
  def extract(self, text):
    splits = re.findall(SEARCHSTRING,text)
    if len(splits[0]) == 1:
      self.abstract = splits[0][0]
      self.extracted_abstract = True
      self.extracted_keywords = False
      print "Just found one text. Potential pitfall in %s" % self.filename
    elif len(splits[0]) == 2:
      self.abstract = splits[0][0]
      self.extracted_abstract = True
      if len(splits[0][1]) < 500:
        self.keywords = splits[0][1]
        self.extracted_keywords = True
      else:
        self.extracted_keywords = False
    else:
      self.extracted_abstract = False
      self.extracted_keywords = False
    
  def clean_keywords(self):
    if self.extracted_keywords:
      self.keywords = self.keywords.replace("1. ","")
      self.keywords = self.keywords.replace(":","")
      self.keywords = self.keywords.replace("1 ","")
      self.keywords = self.keywords.replace("1.","")
      self.keywords = self.keywords.replace("\n"," ")
  
  def remove_difficult_chars(self):
    #See if there is a method which prints the non-valid characters, make a replace function here. 
    return True    


    


#
# Program starts executing here
#
#

for folder in os.listdir(dir_path):
  if os.path.isdir(dir_path+folder) == True:
    for infile in os.listdir(dir_path+folder):
      #print infile
      if infile.endswith(".pdf"):
        workfile = dir_path + folder + "/"+ infile
        try:
          inputfile = file(workfile, "rb")
          print workfile
          proc = subprocess.Popen(["java","-jar","tika-app-1.2.jar","--text", workfile],stdout=subprocess.PIPE)
          text =  proc.stdout.read()
          pdf = PdfDoc(workfile, text)
          documents.append(pdf)
        except Exception as e:
          print "Could not open file: %s, %s" % (workfile,e)
        inputfile.close()
        

## Everything is read, parsed and initially processed. Now its exported
result = open("result.xml","w")
errors = open("errors.txt","w")

# create XML 
root = etree.Element('documents')

for doc in documents: 
  document = etree.Element('document')
  #create the name-node
  name = etree.Element('name')
  name.text = doc.filename
  document.append(name)
  
  #If missing either of abstract or keywords
  if not doc.extracted_abstract or not doc.extracted_keywords: 
    missing_error = "\n-- SOMTEHING IS MISSING--\n IN FILE: %s \n" % doc.filename
    errors.write(missing_error)
    
  
  #if abstract is present
  if doc.extracted_abstract:
    try:
      abstract = etree.Element('abstract')
      abstract.text = doc.abstract
      document.append(abstract)
    except ValueError:
      xml_error = "\n --COULD NOT PRINT ABSTRACT TEXT TO XML DUE TO VALUE ERROR -- \n"
      doc.extracted_abstract = False
      errors.write(xml_error)
  else:
    abstract_error = "\n--COULD NOT EXTRACT ABSTRACT--\n"
    errors.write(abstract_error)
  
  #if keywords are present
  if doc.extracted_keywords:
    try:
      keywords = etree.Element('keywords')
      keywords.text = doc.keywords
      document.append(keywords)
    except ValueError:
      xml_error = "\n --COULD NOT PRINT KEYWORDS TEXT TO XML DUE TO VALUE ERROR -- \n"
      doc.extracted_keywords = False
      errors.write(xml_error)
  else: 
    abstract_error = "\n--COULD NOT EXTRACT KEYWORDS--\n"
    errors.write(abstract_error)
    
      
  #Prints the whole text to error log
  if not doc.extracted_abstract or not doc.extracted_keywords: 
    give_text = "HERE IS THE TEXT: \n %s \n\n -+-+-+-+-+-+-+- \n %s \n\n %s \n END OF %s\n\n\n" % (doc.text, doc.abstract, doc.keywords, doc.filename)
    errors.write(give_text)
    
  # Appending the final document to the root
  root.append(document)

# pretty string
s = etree.tostring(root, pretty_print=True)
print s





