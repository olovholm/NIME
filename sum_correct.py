#!/usr/bin/python
#-*- coding: utf-8

import xml.etree.ElementTree as ET


tree = ET.parse('result.xml')
root = tree.getroot()
documents =  root.findall('document')
print len(documents)