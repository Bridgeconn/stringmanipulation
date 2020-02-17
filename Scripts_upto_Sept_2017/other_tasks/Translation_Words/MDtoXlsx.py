#!/usr/bin/python
# -*- coding: utf-8 -*-

import openpyxl
import re
import os
import sys
import glob
import errno

fno = 0
row = 1
sorted_list = []
mdfiles = glob.glob('TW/**/*.md')
for i in mdfiles:
	filename = i.split('/')[2]
	fn = filename.split('.')[0]
	sorted_list.append((fn, i))
	sorted_list.sort()

for n in sorted_list:
	with open(n[1]) as inputfile:

		# print inputfile
		if row == 1:
			print "Conversion in progress !"
			wb = openpyxl.Workbook()
			sheet = wb.get_sheet_by_name('Sheet')
			sheet['A' + str(row)] = "Translation Word"
			sheet['B' + str(row)] = "Words"
			sheet['C' + str(row)] = "Definition"
			sheet['D' + str(row)] = "Definition_hi"
			sheet['E' + str(row)] = "Facts"
			sheet['F' + str(row)] = "Facts_hi"
			sheet['G' + str(row)] = "Bible References"
			sheet['H' + str(row)] = "Bible References_hi"
			sheet['I' + str(row)] = "Translation Suggestions"
			sheet['J' + str(row)] = "Translation Suggestions_hi"
			sheet['K' + str(row)] = "Bible Examples"
			sheet['L' + str(row)] = "Bible Examples_hi"
			row += 1

		addline = ""
		column = ""
		sheet['A' + str(row)] = n[0]
		for inpline in inputfile:
			process1= re.sub("\(\.\.(\/*\w*\d*)*\.md\)", "", inpline)
			process2 = re.sub("\(rc:(\/*\w*-*\d*)*\)", "", process1)
			line = re.sub("[HG]\d+\s?,?", "", process2)
			if re.search(r"##\s?Definition:\s?", line):
				if column != "":
					sheet[column + str(row)] = addline.strip()
				addline = ""
				column = "C"
			elif re.search(r"##\s?Facts:\s?", line):
				if column != "":
					sheet[column + str(row)] = addline.strip()
				addline = ""
				column = "E"
			elif re.search(r"##\s?Bible References:\s?", line):
				if column != "":
					sheet[column + str(row)] = addline.strip()
				addline = ""
				column = "G"
			elif re.search(r"##\s?Translation Suggestions:?\s?", line):
				if column != "":
					sheet[column + str(row)] = addline.strip()
				addline = ""
				column = "I"
			elif re.search(r"##\s?Examples from the Bible stories:\s?", line):
				if column != "":
					sheet[column + str(row)] = addline.strip()
				addline = ""
				column = "K"
			elif re.search(r"##\s?Word Data:?\s?", line):
				if column != "":
					sheet[column + str(row)] = addline.strip()
				addline = ""
				column = "M"
			elif re.search(r"#(\s*\w*,*'*-*\(*\)*)*", line) and line[1] != "#":
				if column != "":
					sheet[column + str(row)] = addline.strip()
				addline = ""
				column = ""
				sheet['B' + str(row)] = str(line[2:-3])
			else:
				addline += line
				if column == "":
					print line
		sheet[column + str(row)] = addline.strip()
		row += 1

		if row > 100:
			fno += 1
			filen = "Terms" + str(fno) + ".xlsx"
			print filen
			wb.save(filename=filen)
			row = 1
			print 'Conversion Done ! ' + filen

fno += 1
filen = "Terms" + str(fno) + ".xlsx"
print filen
wb.save(filename=filen)
row = 1
print 'Conversion Done ! ' + filen
