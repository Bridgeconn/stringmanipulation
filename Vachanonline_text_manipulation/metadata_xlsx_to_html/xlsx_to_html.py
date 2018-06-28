'''
	The script is for generating about.html file's for Bible Metadata from excel file.
'''

import glob
import os
import re
from openpyxl import load_workbook
import openpyxl

'''Reading the excel file'''
excel_file = "Bible Metadata.xlsx"
if os.path.exists(excel_file):
	work_book = load_workbook(excel_file)
	sheet = work_book.get_sheet_names()
	worksheet = work_book.get_sheet_by_name(sheet[0])
	work_book.active

	'''Extracting the column name'''
	dt_1 = worksheet["A1"].value
	dt_2 = worksheet["B1"].value
	dt_3 = worksheet["D1"].value
	dt_4 = worksheet["E1"].value
	dt_5 = worksheet["F1"].value
	dt_6 = worksheet["K1"].value
	dt_7 = worksheet["L1"].value
	dt_8 = worksheet["S1"].value
	dt_9 = worksheet["T1"].value

	html_content = ""
	row = 2

	'''Extracting the data for each bible from each row and column'''
	for row in range(2,13 + 1):	
		dd_1 = worksheet["A" + str(row)].value
		dd_2 = worksheet["B" + str(row)].value
		dd_3 = worksheet["D" + str(row)].value
		dd_4 = worksheet["E" + str(row)].value
		dd_5 = worksheet["F" + str(row)].value
		dd_6 = str(worksheet["K" + str(row)].value)
		dd_7 = str(worksheet["L" + str(row)].value)
		dd_8 = worksheet["S" + str(row)].value
		dd_9 = worksheet["T" + str(row)].value

		'''Adding the tags and data's into single variable'''
		html_content = "<dt>" + dt_1 + "</dt>\n" + "<dd>" + dd_1 + "</dd>\n" + "<dt>" + dt_2 + "</dt>\n" + "<dd>" + dd_2 + "</dd>\n" + "<dt>" 
		html_content += dt_3 + "</dt>\n" + "<dd>" + dd_3 + "</dd>\n" + "<dt>" + dt_4 + "</dt>\n" + "<dd>" + dd_4 + "</dd>\n"
		html_content += "<dt>" + dt_5 + "</dt>\n" + "<dd>" + dd_5 + "</dd>\n" 

		if dd_6:
			html_content += "<dt>" + dt_6 + "</dt>\n" + "<dd>" + dd_6 + "</dd>\n" 
		
		if dd_7:
			html_content += "<dt>" + dt_7 + "</dt>\n" + "<dd>" + dd_7 + "</dd>\n"
		
		html_content += "<dt>" + dt_8 + "</dt>\n" + "<dd>" + dd_8 + "</dd>\n" + "<dt>" + dt_9 + "</dt>\n" + "<dd>" + dd_9 + "</dd>\n"

		'''For removing the float value like "2018.0" to "2018" '''
		html_final = re.sub(r"(\.0)","",html_content)

		'''Creating a folder with language name or accessing the folder'''
		if os.path.exists(dd_4):
			os.chdir(dd_4)
			'''Generating an about.html file in the language folder and writing the content to it.'''
			html_file = open("about.html", 'w', encoding = "utf-8")
			html_file.write(html_final)
			os.chdir("..")
		else:
			os.mkdir(dd_4)
			os.chdir(dd_4)
			html_file = open("about.html", 'w', encoding = "utf-8")
			html_file.write(html_final)
			os.chdir("..")

		print(html_final)
		html_content = ""