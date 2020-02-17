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
    sheet = wb.get_sheet_by_name('Sheet1')
    for row in range(2, sheet.max_row):

        chapter = sheet['B' + str(row)].value
        if len(chapter) < 2:
            chapter = '0' + chapter

        if not os.path.exists('%s/%s' %(folder, chapter)):
            os.mkdir("%s/%s/" %(folder, chapter))

        verse = sheet['C' + str(row)].value

        v = str(verse).split('-')
        if len(v[0]) < 2:
            v[0] = '0' + v[0]
        chunk = v[0] + ".md"

        outfile = open('%s/%s/%s' %(folder, chapter, chunk), "w")
        name = sheet['E' + str(row)].value
        n = unicode(name).encode('utf-8')
        if name == None:
            outfile.write(" ")
        else:
            q = n.replace("પ્રશ્ન?", "# ")
            a = q.replace("જવાબ.", "\n\n")
            b = a.replace("પ્ર?", "# ")
            c = b.replace("જ.", "\n\n ")
            d = c.replace("પ્રશ્ન:", "# ")
            e = d.replace("જવાબ:", "\n\n")
            g = e.replace("ઉત્તર:", "\n\n")
            h = g.replace("પ્રશ્ન.", "# ")
            outfile.write(h.strip())
            outfile.write("\n")

        outfile.close()

    # Close the file
    wb.close()
    print 'Conversion Done !'
