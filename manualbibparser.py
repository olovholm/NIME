#!/usr/bin/python
#-*- coding: utf-8

import os, re, sys, traceback
import xml.etree.ElementTree as ET
from pybtex.database.input import bibtex

URL_PATTERN = re.compile('nime\d{4}_\d{3}.pdf',re.IGNORECASE)
BLOCK_START = re.compile('@inproceedings\{') # after here comes title 
CAT_PATTERN = re.compile('w =',re.IGNORECASE) # Beginning of line. Including an equels sign
CONTENT_PATTERN = re.compile('\{(.*)\}',re.IGNORECASE) # On line with cat_pattern {(between braces)}
BLOCK_END = re.compile('') # Single curly brace on line }

dir_path = r"nime_archive/nime/bibtex/"
result_path = 'result_cleaned.xml'
tree = ET.parse(result_path)
root = tree.getroot()
global exception_cnt
global texts_cnt
exception_cnt = 0
texts_cnt = 0

for infile in os.listdir(dir_path):
    print "Starting parsing file %s" % infile
    if infile.endswith(".bib"):
      print infile
      doc = open(dir_path+infile)
      for line in doc:
        
      