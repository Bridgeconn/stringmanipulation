'''
 To compare the old and new translations in a same file and 
 write the difference into next column 
'''

import openpyxl
import glob
import os
import re

files = sorted(glob.glob("*.xlsx"))

for file in files:
	'''Loading the excel file'''
	load_file = openpyxl.load_workbook(file)
	file_sheets = load_file.get_sheet_names()
	file_sheet = load_file.get_sheet_by_name(file_sheets[0])
	load_file.active

	cwd = os.getcwd()
	file_path = cwd + "/" + file
	'''Giving the column heading manually'''
	file_sheet['F' + str(1)] = "Difference"

	for rows in range(2, file_sheet.max_row + 1):
		'''Reading the verses row by row'''
		new_verse = file_sheet['D' + str(rows)].value
		old_verse = file_sheet['E' + str(rows)].value
		
		dif_ver = []
		differences = ""
		if new_verse:
			new_versus = new_verse.split("\n•")
		
			if old_verse:
				old_versus = old_verse.split("\n•")

				for new in new_versus:
					'''Fetching the verse line by line'''
					if new:
						for old in old_versus:
							if old:
								if new == old:
									print("")
			
								else:
									if "•"+ new != "\n":
										if new not in dif_ver:
											'''Adding the content into list'''
											dif_ver = "•"+ new
							else:
								if new not in dif_ver:
									dif_ver = "•"+ new
						differences += dif_ver
				
				'''Aligning the content'''
				diff = re.sub(r'•','\n•',differences)
				
				'''Writing into excel'''
				file_sheet['F' + str(rows)] = diff
				load_file.save(file_path)

			else:
				new = file_sheet['D' + str(rows)].value
				
				file_sheet['F' + str(rows)] = new
				load_file.save(file_path)