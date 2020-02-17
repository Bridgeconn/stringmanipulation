'''
 Converting the md files in the folders and sub-folders into
 Doc file with all the details of folders, subfolders and md files
'''
# -*- coding: utf-8 -*-


import os
import glob
import re

def generate_doc(path, book,):
	'''Opens a new file in given path'''
	file = open(path, "w")

	'''Writes the content into file'''
	file.write(book)
	file.close()

'''Accessing current directory''' 
cwd = os.getcwd()

'''Fetching all the folders'''
folder = glob.glob("**/")
book = ""
chapters = ""
verse = ""
note = ""

for book_folder in folder:
	book_name = re.sub(r"/","",book_folder)
	book = "Book : " + book_name + "\n"
	
	'''Changing the directory'''
	os.chdir(book_folder)
	
	'''Here the chapter folders are being fetched and sorted'''
	sub_folder = sorted(glob.glob("**/"))

	for chapter_folder in sub_folder:
		chapter_number = re.sub(r"/","",chapter_folder)
		book += "Chapter : " + chapter_number + "\n"
		os.chdir(chapter_folder)
		
		'''Fetching and sorting all md files'''
		md_files = sorted(glob.glob("*.md"))

		for files in md_files:
			file = re.sub(r".md","",files)
			book += "Verse : " + file + "\n\n"
			
			'''Reads the content from the md file'''
			doc = open(files).read()
			final_doc = re.sub(r"\n\n","\n",doc)
			
			'''Aligning all the content and merging'''
			book += final_doc + "\n\n"
			doc_file = book_name + ".doc"

		'''reverse the directory'''
		os.chdir("..")	

	os.chdir("..")
	
	'''Calling the function for generation doc file'''
	generate_doc(doc_file, book)