#!/usr/bin/python
#-*- coding: utf-8

import os, re, sys, traceback, time
import xml.etree.ElementTree as ET
from pybtex.database.input import bibtex

URL_PATTERN = re.compile('nime\d{4}_\d{3}.pdf',re.IGNORECASE)
BLOCK_START = re.compile(r'@inproceedings{([:.\w]*)$', re.IGNORECASE) # after here comes title 
CAT_PATTERN = re.compile(r'^(.*) =',re.IGNORECASE) # Beginning of line. Including an equels sign
CONTENT_PATTERN = re.compile(r'{(.*)}') # On line with cat_pattern {(between braces)}
BLOCK_END = re.compile('^[}\s]*$') # Single curly brace on line }

dir_path = r"nime_archive/nime/bibtex/"
result_path = 'result_cleaned.xml'
tree = ET.parse(result_path)
root = tree.getroot()
global exception_cnt
global texts_cnt
exception_cnt = 0
texts_cnt = 0

def regexread():
  """
for infile in os.listdir(dir_path):
    print "Starting parsing file %s" % infile
    if infile.endswith(".bib"):
      
      print infile
      doc = open(dir_path+infile)
      for line in doc:
        bs = BLOCK_START.search(line)
        if bs != None:
          print bs.group(1)
        cat = CAT_PATTERN.search(line)
        if cat != None:
          print cat.group(1)
        co = CONTENT_PATTERN.search(line)
        if co != None:
          print co.group(1)
        be = BLOCK_END.search(line)
        if be != None:
          print be.group(0)
"""



def seekread(): 
  for infile in os.listdir(dir_path):
      print "Starting parsing file %s" % infile
      if infile.endswith(".bib"):
        elements = {}
        doc = open(dir_path+infile).read()
        i = 0
        while i>-1:
          element = {}
          i = doc.find('{',i)
          nameend = i+1
          while not doc[nameend].isspace() and doc[nameend] != ',':
            nameend = nameend + 1
          #print doc[i+1:nameend]
          j = readbraces(i+1,doc)
          while i >-1:
            i, key, val= readelement(i,doc)
            if i < 0:
              break
            element[key] = val
          '''
          k = readnontoken(i+1, doc)
          if doc[k].isalpha():
            i = k 
            k = readtoken(i,doc)
            print doc[i:k]
          else: 
            i = k
            k = readbraces(i+1, doc)
            print doc[i:k]
            '''
          #print "HER:",element
          try:
            print element["url"]
          except KeyError as e:
            print e
          elements.update(element)
          i = j


          
        
def readbraces(i, doc):
  inn = doc.find('{',i)
  ut = doc.find('}',i)
  while inn > -1 and inn < ut:
    i = readbraces(inn+1, doc)
    if i == -1:
      return -1
    inn = doc.find('{',i)
    ut = doc.find('}',i)
  if ut > -1:
    ut = ut + 1
  return ut

def readtoken(i, doc):
  while doc[i].isalnum():
    i = i + 1
    if i >= len(doc):
      return -1
  return i
  
def readnontoken(i, doc):
  while not doc[i].isalpha() and not doc[i]=='{':
    i = i + 1
    if i >= len(doc):
      return -1
  return i
  
def readelement(i,doc):
  j = doc.find('=',i)
  i = doc.find('}',i)
  if i < j: 
    return -1, "", ""
  k = doc.find('{',j)
  m = readbraces(k+1,doc)
  
  while not doc[j].isalnum():
    j = j - 1
  l = j+1
  while doc[j].isalnum():
    j = j - 1
  return m, doc[j+1:l], doc[k+1:m-1] 
      
seekread()