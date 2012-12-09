#!/usr/bin/python
#-*- coding: utf-8

import os
from pybtex.database.input import bibtex

dir_path = "nime_archive/nime/bibtex/"
num_texts = 0

class Bibfile:
  def __init__(self,bibs):
    self.bibs = bibs
    for a in self.bibs.entries.keys():
      num_text += 1
       print bibs.entries[a].fields['title']
       #Need to implement a way of getting just the nime-identificator
       try:
         print bibs.entries[a].fields['url']
       except:
         print "couldn't find URL for text: %s " % a
      
    
    print "creating new bibfile"



bibfiles = []
parser = bibtex.Parser()


for infile in os.listdir(dir_path):
    if infile.endswith(".bib"):
      print infile
      bibfiles = Bibfile(parser.parse_file(dir_path+infile))