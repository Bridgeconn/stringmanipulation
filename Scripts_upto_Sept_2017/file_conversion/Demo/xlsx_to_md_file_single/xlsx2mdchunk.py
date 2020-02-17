#!/usr/bin/python
# -*- coding: utf-8 -*-

import openpyxl
import re
import os

# Open xlsx file
wb = openpyxl.load_workbook('2 Corinthian-L3.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

# Open txt file for writing
p = re.compile(u"\u2022")
q = re.compile('- ')
prev_book = ""
prev_chapter = ""
book = ""
chapter = ""

# Access each element of a column row by row and write it to txt file
for row in range(2, sheet.max_row):

    book = sheet['A' + str(row)].value
    if  prev_book != str(book):
        os.mkdir(book)

    chapter = sheet['B' + str(row)].value
    if prev_chapter != str(chapter):
        os.mkdir("%s/%s/" %(book,chapter))

    verse = sheet['C' + str(row)].value
    v = str(verse).split('-')
    chunk = v[0] + ".md"
    outfile = open('%s/%s/%s' %(book,chapter,chunk), "w")
    name = sheet['D' + str(row)].value
    name = p.sub('# ', name)
    name = q.sub('\n', name)
    outfile.write(unicode(name).encode('utf-8').strip())
    outfile.write("\n\n")
    outfile.close()
    prev_book = book
    prev_chapter = chapter

# Close the file

wb.close()
print 'Conversion Done !'
