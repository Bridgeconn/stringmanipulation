#!/usr/bin/python
# -*- coding: utf-8 -*-

import openpyxl
import re

# Open xlsx file
wb = openpyxl.load_workbook('2_Corinthian-L3.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

# Open txt file for writing
outfile = open("2_Corinthian-L3.md", "w")

p = re.compile(u"\u2022")
q = re.compile('- ')

# Access each element of a column row by row and write it to txt file
for row in range(2, sheet.max_row):
    name = sheet['E' + str(row)].value
    name = p.sub('# ', name)
    name = q.sub('\n', name)
    outfile.write(unicode(name).encode('utf-8').strip())
    outfile.write("\n\n")

# Close the file
outfile.close()
wb.close()
print 'Conversion Done !'
