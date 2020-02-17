import openpyxl

# Open xlsx file
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

# Open txt file for writing
outfile = open("output.txt", "w")

# Access each element of a column row by row and write it to txt file
for row in range(1, sheet.max_row + 1):
    name = sheet['C' + str(row)].value
    outfile.write(name)
    outfile.write("\n")

# Close the file and print result
outfile.close()
print 'Done.'
