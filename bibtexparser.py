#!/usr/bin/python
#-*- coding: utf-8

import os
from pybtex.database.input import bibtex

URL_PATTERN = "\/d{4}\/nime[d{4}]_d{3}.pdf" # Not totally correct, but idea embedded

dir_path = "nime_archive/nime/bibtex/"
num_texts = 0

#Open and parse the XML structure created from the results of the extraction processs

class Bibfile:
  def __init__(self,bibs):
    self.bibs = bibs
    num_text = 0 
    for a in self.bibs.entries.keys():
       num_text += 1
       #print bibs.entries[a].fields['title']
       #Need to implement a way of getting just the nime-identificator
       try:
         print bibs.entries[a].fields['url'] 
         # Do a search for file. 
         # Search up id in the XML with results. 
       except:
         print "couldn't find URL for text: %s " % a
      
    
    print "creating new bibfile"



bibfiles = []
parser = bibtex.Parser()


for infile in os.listdir(dir_path):
    print "Starting parsing file %s" % infile
    if infile.endswith(".bib"):
      print infile
      bibfiles = Bibfile(parser.parse_file(dir_path+infile))