#!/usr/bin/python
#-*- coding: utf-8

import os

dir_path = "nime_archive/nime/bibtex/"

class Bibfile:
  def __init__(self,text):
    self.text = text
    print self.text
    
    print "creating new bibfile"



bibfiles = []

for infile in os.listdir(dir_path):
    if infile.endswith(".bib"):
      print infile
      bibfiles = Bibfile(open(dir_path+infile).read())