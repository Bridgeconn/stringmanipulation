

import openpyxl
import glob
import os
import re

files = sorted(glob.glob("*.xlsx"))

for file in files:
	print(file)
	load_file = openpyxl.load_workbook(file)
	file_sheets = load_file.get_sheet_names()
	file_sheet = load_file.get_sheet_by_name(file_sheets[0])
	load_file.active

	cwd = os.getcwd()
	file_path = cwd + "/" + file
	file_sheet['F' + str(1)] = "Difference"

	for rows in range(2, file_sheet.max_row + 1):
		
		new_verse = file_sheet['D' + str(rows)].value
		#print(new_verse)
		old_verse = file_sheet['E' + str(rows)].value
		#print(old_verse)
		dif_ver = []
		differences = ""
		if new_verse:
			new_versus = new_verse.split("\n•")
			#print(new_versus)
			if old_verse:
				old_versus = old_verse.split("\n•")

				for new in new_versus:
					#print(new)
					if new:
						for old in old_versus:
							if old:
								if new == old:
									print("")
									#print("New-------",new)
									#print("Old-------",old)
								else:
									if "•"+ new != "\n":
										if new not in dif_ver:
											dif_ver = "•"+ new
							else:
								#if "•"+ new != "\n":
								if new not in dif_ver:
									dif_ver = "•"+ new
						differences += dif_ver
				
				diff = re.sub(r'•','\n•',differences)
				#print(diff,rows)
				file_sheet['F' + str(rows)] = diff
				load_file.save(file_path)

			else:
				new = file_sheet['D' + str(rows)].value
				#print(new,rows)
				#new = new_versus
				file_sheet['F' + str(rows)] = new
				load_file.save(file_path)