'''
Converting docx files to usfm format by adding the tag's.
The chapter and verse number's are given in bold are being
used to seperate the content.
'''

from docx import Document
import glob
import os
import re
from openpyxl import load_workbook
import openpyxl

'''Checking the docx directory and accessing it.'''
try:
	if not os.path.exists("docx"):
		print("No folder for docx, Create a folder with name \"docx\" and drop docx file in that")
	else:
		os.chdir("docx")
except OSError:
	print ('Error: Creating directory.' + "docx")

files = glob.glob("*.docx")

for docx_file in files:
	content = ""
	file_name = re.sub(r".docx","",docx_file)

	'''Reading the contents from docx file'''
	document = Document(docx_file)

	'''Searching the bold character's for spliting the content '''
	for para in document.paragraphs:
		for run in para.runs:
			if run.bold:
				search_number = re.match(r"(\d+\:\d+)",run.text)
				if search_number:
					content += "\n" + run.text
				else:
					content += run.text
			else:
				content += run.text

	os.chdir("..")

	'''Creating a folder to store usfm files'''
	try:
		if not os.path.exists(file_name):
			os.makedirs(file_name)
			os.chdir(file_name)
		else:
			os.chdir(file_name)
	except OSError:
		print ('Error: Creating directory.' + file_name)

	'''Aligning the content'''
	align_doc = re.sub(r"(\\id )","\n\\id ",content)
	note = align_doc.split("\n")
	notes = ""

	for row in note:
		if row:

			'''Regex used for extraction of required content'''
			search_id = re.match(r"(\\id .*)",row)
			search_chapter = re.match("(\d+)\:(\d+) (.*)",row)
			search_verse = re.match("(\d+)\:(\d+) (.*)",row)
			
			if search_id:
				if notes:
					'''Final content is been added to the usfm by adding tags'''
					print(notes)
					usfm_file.write(notes)
					notes = ""
				
				chapter = ""
				previous_chapter = ""
				verse = ""
				book = ""
				book = search_id.group(1)
				book_name = re.sub(r"\\id ","",book)

				'''Creating an usfm file with the name of book'''
				usfm_file = open(book_name + ".usfm", "w")
				notes += book + "\n"
			
			'''Adding the tags for chapter and verse.'''
			if search_chapter:
				chapter = search_chapter.group(1)

				'''To remove the repeatition and duplicates from chapter'''
				if str(chapter) != str(previous_chapter):
					notes += "\\c " + chapter + "\n"
					previous_chapter = chapter

			if search_verse:
				verse = search_verse.group(2)
				notes += "\\v " + verse + "\n\\f " + search_verse.group(3) + "\n"
	
	'''Writing into usfm file'''
	print(notes)
	usfm_file.write(notes)
	notes = ""
os.chdir("..")