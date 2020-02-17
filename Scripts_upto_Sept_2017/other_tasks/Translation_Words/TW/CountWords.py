#!/usr/bin/python
# -*- coding: utf-8 -*-

import openpyxl
import re
import os
import sys
import glob
import errno

yourtext = ""
mdfiles = glob.glob('kt/*.md')
for i in mdfiles:
	with open(i) as inputfile:
		for inpline in inputfile:
			if re.search("Bible References", inpline):
				break
			else:
				process1 = re.sub("\(\.\.(\/*\w*\d*)*\.md\)", "", inpline)
				process2 = re.sub("\(rc:(\/*\w*-*\d*)*\)", "", process1)
				process3 = re.sub("\d+", "",process2)
				# process4 = re.sub("\-", " ",process3)
				process5 = re.sub("\(?\)?\[?\]?\.?\_?\*?\,?\??\!?", "",process3)
				process6 = re.sub("#{1,2}","",process5)
				process7 = re.sub(":", "", process6)
				process8 = re.sub("\"", "", process7)
				line = re.sub("[HG]\d+\s?,?", "", process8)
				yourtext += " " + line
words = yourtext.split(" ")
uniqueword = set(words)
# print uniqueword
n = 0; m = 1
for i in words:
	n += 1
for j in uniqueword:
	print j
	m += 1
print "Total Words: " + str(n)
print "Unique Words: " + str(m) 

print 'Counting Done !'