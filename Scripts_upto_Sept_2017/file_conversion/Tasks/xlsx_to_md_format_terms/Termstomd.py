#!/usr/bin/python
# -*- coding: utf-8 -*-

import openpyxl
import re
import os
import sys
import glob
import errno

# Open xlsx file
files = glob.glob('**/*.xlsx')
for name in files:
    file_name = name.split('/')[1]
    print file_name

    wb = openpyxl.load_workbook(name)

    # Initialization of variables
    chapter = ""
    f = file_name.split('.')
    folder = f[0]

    # Check if directory exists
    if not os.path.exists(folder):
        os.mkdir(folder)
    print "Conversion in progress !"

    # Access each element of a column row by row and write it to md file
    sheet = wb.get_sheet_by_name('Explanation')
    prev_name = ""

    for row in range(2, sheet.max_row):

        name = sheet['C' + str(row)].value
        if name != None:
        	if re.search(r',', name):
        		name = name.split(',')[0]
        	chunk = name + ".md"
        	outfile = open('%s/%s' %(folder, chunk), "w")
        	if prev_name != name and prev_name != "":
        		outfile.close
        else:
        	prev_name = name


        word = sheet['D' + str(row)].value
        if word != None:
        	terms = "# " + word + " #\n"
        	outfile.write(terms.encode('utf-8'))
        	definition = "\n" + sheet['F' + str(row)].value + "\n"
        	outfile.write(definition.encode('utf-8'))
        else:
        	if sheet['E' + str(row)].value == "Translation Suggestions":
        		suggestion = "\n\n## " + sheet['F' + str(row)].value + ": ##\n"
        		outfile.write(suggestion.encode('utf-8'))
        	else:
        		description = "\n * " + sheet['F' + str(row)].value
        		outfile.write(description.encode('utf-8'))


    # Close the file
    wb.close()
    print 'Conversion Done !'
