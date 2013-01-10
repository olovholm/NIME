#!/usr/bin/python
#-*- coding: utf-8

import os, re, sys
import xml.etree.ElementTree as ET
from pybtex.database.input import bibtex

URL_PATTERN = re.compile('nime\d{4}_\d{3}.pdf',re.IGNORECASE)

dir_path = r"nime_archive/nime/bibtex/"
result_path = 'result_cleaned.xml'
tree = ET.parse(result_path)
root = tree.getroot()

## Reading the document structure

results = {}

for document  in root.iter('document'):
  name = document.find('name').text
  results[name] = {}
  print document.find('name').text
  if document.find('abstract') != None:
     results[name]['abstract'] = document.find('abstract').text
  if document.find('keywords') != None:
     results[name]['keywords'] = document.find('keywords').text



num_texts = 0

#Open and parse the XML structure created from the results of the extraction processs

class Bibfile:
  def __init__(self,bibs):
    self.bibs = bibs
    num_text = 0 
    for a in self.bibs.entries.keys():
       num_text += 1
       #print bibs.entries[a].fields['title']
       try:
         #print bibs.entries[a].fields['url'] 
         # Do a search for file. 
         res = re.findall(URL_PATTERN,bibs.entries[a].fields['url'])
         if res > 0:
           bibs.entries[a]['abstract'] = results[res[0]]['abstract']
           bibs.entries[a]['keywords'] = results[res[0]]['keywords']
           #print res[0]
         # Search up id in the XML with results. 
       except Exception as e:
         print "couldn't find URL for text: %s " % e
      



bibfiles = []
parser = bibtex.Parser()


for infile in os.listdir(dir_path):
    print "Starting parsing file %s" % infile
    if infile.endswith(".bib"):
      print infile
      bibfiles = Bibfile(parser.parse_file(dir_path+infile))
      
