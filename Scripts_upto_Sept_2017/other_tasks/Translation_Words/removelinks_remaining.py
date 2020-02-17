#!/usr/bin/python
# -*- coding: utf-8 -*-

import openpyxl
import re
import os
import sys
import glob
import errno

folder = "Translation_Words"
prev_word = ""
if not os.path.exists(folder):
	os.mkdir(folder)

sorted_list = []
excludedwords = []
mdfiles = glob.glob('TW/**/*.md')
for i in mdfiles:
	filename = i.split('/')[2]
	fn = filename.split('.')[0]
	sorted_list.append((fn, i))
	sorted_list.sort()

titusfiles = glob.glob('Titus_TW/*.md')
for name in titusfiles:
	file_name = name.split("/")[1]
	word_name = file_name.split(".")[0]
	excludedwords.append(word_name)

# print excludedwords
for n in sorted_list:
	if n[0] not in excludedwords:
		if n[0] != prev_word:
			prev_word = n[0]
			inputfile = open(n[1]).read()
			process1 = re.sub("\(\.\.(\/*\w*\d*)*\.md\)", "", inputfile)
			process2 = re.sub("\(rc:(\/*\w*-*\d*)*\)", "", process1)
			output = re.sub("[HG]\d+\s?,?", "", process2)
			outfile = open('%s/%s' %(folder, n[1].split("/")[2]), "w")
			outfile.write(output)
			outfile.close()
			print n[1].split("/")[2] + " completed"

print 'Conversion Done !'