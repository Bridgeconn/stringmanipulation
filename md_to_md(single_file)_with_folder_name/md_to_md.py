'''
 Converting the md files in the folders and sub-folders into
 single md file with all the details of folders, subfolders and md files
 Along with a heading for each questions with book name,chapter & verse number
'''
# -*- coding: utf-8 -*-


import os
import glob
import re


def generate_md(path, book,):
	'''Opens a new file in given path'''
	file = open(path, "w")
	'''Writes the content into file'''
	file.write(book)
	file.close()


''' Accessing current directory '''
cwd = os.getcwd()

'''Fetching all the folders'''
folder = glob.glob("**/")

for book_folder in folder:
	book_name = re.sub(r"/","",book_folder)
	book = ""
	verse = ""
	note = ""
	
	'''Changing the directory'''
	os.chdir(book_folder)
	
	'''Here the chapter folders are being fetched and sorted'''
	sub_folder = sorted(glob.glob("**/"))

	for chapter_folder in sub_folder:
		chapter_number = re.sub(r"/","",chapter_folder)
		os.chdir(chapter_folder)

		'''Fetching and sorting all md files'''
		md_files = sorted(glob.glob("*.md"))

		for files in md_files:
			verse = re.sub(r".md","",files)

			'''Reads the content from the md file'''
			doc = open(files).read()
			final_doc = re.sub(r"\n\n","\n",doc)
			
			'''Aligning all the content and merging'''
			book += "++Content from " + book_name + " " + chapter_number + ":" + verse + ".md++\n"
			book += final_doc + "\n\n"
			md_file = book_name + ".md"

		'''reverse the directory'''
		os.chdir("..")	

	os.chdir("..")
	
	'''Calling the function for generatingmd file'''
	generate_md(md_file, book)