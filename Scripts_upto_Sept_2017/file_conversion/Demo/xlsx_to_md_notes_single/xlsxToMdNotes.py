#!/usr/bin/python
# -*- coding: utf-8 -*-

import openpyxl
import re
import os

# Open xlsx file
print "Enter file name (with extension):"
filename = raw_input('> ')
wb = openpyxl.load_workbook(filename)

# Initialization of variables
pattern = re.compile(r'-')
verse = ""
chapter = ""
prev_verse = ""
f = filename.split('.')
folder = f[0]

# Check if directory exists
if not os.path.exists(folder):
    os.mkdir(folder)
print "Conversion in progress"

# Access each element of a column row by row and write it to md file
sheet = wb.get_sheet_by_name(folder)
for row in range(1, sheet.max_row):

    # Read chapter number and verse number
    idnum = str(sheet['B' + str(row)].value)
    if pattern.search(idnum):
        idno = idnum.split('-')
        chapter = idno[0]
        verse = idno[1]
        if not os.path.exists('%s/%s' %(folder, chapter)):
            os.mkdir("%s/%s/" %(folder, chapter))
    else:
        verse = prev_verse

    # Read reference
    ref = sheet['C' + str(row)].value
    if ref == None:
        ref = " "

    # Read text associated with reference
    text = sheet['D' + str(row)].value
    if text == None:
        text = " "

    # Write data into separate md files 
    if verse == prev_verse:
        outfile = open('%s/%s/%s.md' %(folder,chapter,verse), "a")
        outfile.write("\n\n# " + unicode(ref).encode('utf-8').strip())
    else:
        outfile = open('%s/%s/%s.md' %(folder,chapter,verse), "w")
        outfile.write("# " + unicode(ref).encode('utf-8').strip())

    outfile.write("\n " + unicode(text).encode('utf-8').strip())
    outfile.close()
    prev_verse = verse


# Close the file
wb.close()
print 'Conversion Done !'
