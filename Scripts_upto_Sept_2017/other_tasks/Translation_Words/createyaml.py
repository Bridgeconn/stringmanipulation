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
mdfiles = glob.glob('Titus_TW/*.md')
for i in mdfiles:
	filename = i.split('/')[1]
	fn = filename.split('.')[0]
	sorted_list.append((fn, i))
	sorted_list.sort()

# print sorted_list
titusulb = glob.glob('NT-Hii-SFM/*.SFM')
outfile = open("config.yaml", "w")
outfile.write("---\n")
for file in sorted_list:
	print file[0]
	outfile.write(file[0] + ":\n")
	outfile.write("  false_positives: []\n")
	outfile.write("  occurrences:\n")

	inputfile = open(file[1]).readlines()
	words = inputfile[0][5:-3]
	word = words.split(",")
	for num in word:
		for name in titusulb:
			searchfile = open(name).readlines()
			for searchline in searchfile:
				if re.search("\id ", searchline):
					book_name = searchline[4:7]
				if re.search("\c ", searchline):
					chapter = searchline[3:].strip()
				if re.search(r"\\v", searchline):
					verse = (searchline[3:].split(" ")[0]).strip()
				if re.search(num.strip(), searchline):
					if not re.search("\\\\s", searchline):
						if not re.search("\\\\h", searchline):
							if not re.search("\\\\toc", searchline):
								# print searchline.strip()
								outfile.write("  - rc://hi/ulb/book/" + book_name.lower() + "/" + chapter + "/" + verse + "\n")

print 'Conversion Done !'
