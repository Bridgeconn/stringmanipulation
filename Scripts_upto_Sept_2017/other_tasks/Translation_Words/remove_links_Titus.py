#!/usr/bin/python
# -*- coding: utf-8 -*-

import openpyxl
import re
import os
import sys
import glob
import errno

# Open xlsx file
files = glob.glob('TW/*.xlsx')
for name in files:
    file_name = name.split('/')[1]
    print file_name

    wb1 = openpyxl.load_workbook(name)
    
    print "Conversion in progress !"

    # Access each element of a column row by row and write it to md file
    sheet1 = wb1.get_sheet_by_name('Sheet1')
    folder = file_name.split('.')[0]
    if not os.path.exists(folder):
		os.mkdir(folder)

    mdfiles = glob.glob('TW/**/*.md')
    prev_word = ""

    for row1 in range(1, sheet1.max_row+1):

		for i in mdfiles:
			filename = i.split('/')[2]
			fn = filename.split('.')[0]

			word = sheet1['A' + str(row1)].value
			if word != None:
				if prev_word != word:
					if word == fn:
						prev_word = word
						inputfile = open(i).read()
						process1 = re.sub("\(\.\.(\/*\w*\d*)*\.md\)", "", inputfile)
						process2 = re.sub("\(rc:(\/*\w*-*\d*)*\)", "", process1)
						output = re.sub("[HG]\d+\s?,?", "", process2)
						outfile = open('%s/%s' %(folder, filename), "w")
						outfile.write(output)
						outfile.close()
						print filename + " completed"
    wb1.close()
    print 'Conversion Done !'