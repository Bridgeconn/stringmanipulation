# To convert the excel file into markdown row vise


import openpyxl
import os
import re
import glob

files = glob.glob('*.xlsx')
for filename in files:
	file = filename.split(".")
	wb = openpyxl.load_workbook(filename)
	sheet = wb.get_sheet_by_name('Sheet1')
	wb.active
	# This function is to make new directory
	def createfolder(directory):
	    try:
	        if not os.path.exists(directory):
	            os.makedirs(directory)
	    except OSError:
	        print ('Error: Creating directory.' + directory)

	def book(book_name):
		createfolder(book_name)
		os.chdir(book_name)	# For directory change

	def chapters(chapter_number):
		str1 = (str(chapter_number))
		if len(str1) < 2:
			str1 = '0' + str1	# Adding the 0 for single digit
		
		createfolder(str1)
		os.chdir(str1)	# Changing the directory 

	def notes(verse_number,note):
		
		#Here it match the verse number to get first verse number
		findme = re.match(r"(\d+)(-\d+)?",verse_number,re.M|re.I) 
		verses = findme.group(1)
		if len(verses) < 2:
			verses = '0' + verses

		# Replace • to #
		searchobj = re.sub(r'•','#',note)
		replace_obj = re.sub(r'-','\n',searchobj)
		filename = (verses+".md")	# Adding file extension
		file = open(filename,'w')
		file.write(replace_obj)		# Writing into the new .md file
		os.chdir("..")				# To go back to previous directory
		os.chdir("..")				# To go back to previous directory

	# Reading from the second row
	for row in range(2, sheet.max_row):
		#book_name  = sheet['A' + str(row)].value
		book_name = file[0]
		chapter_number  = sheet['B' + str(row)].value
		verse_number = sheet['C' + str(row)].value
		note = sheet['D' + str(row)].value
		book(book_name)				# Calling the book function
		chapters(chapter_number)	# Calling the chapters function
		notes(verse_number,note)	# Calling notes by passing verse_number and notes