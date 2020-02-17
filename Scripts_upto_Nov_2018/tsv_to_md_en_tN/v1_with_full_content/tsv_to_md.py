'''
The script is written for extracting the required data from .tsv file and create .md files for the data.

	NOTE :
		Please Delete the Old md file before you run this code each time, 
		else the file will rewrite the same content again and again.
'''


import openpyxl
import csv
import os
import re
import glob


''' This function is to make new directory '''
def createfolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory.' + directory)

def book_name(book):
	print(book)
	createfolder(book)
	'''For directory change'''
	os.chdir(book)	

'''Adding the 0 for single digit'''
def chapters_number(chapter):
	str1 = (str(chapter))
	if len(str1) < 2:
		str1 = '0' + str1	
		
	createfolder(str1)
	os.chdir(str1)

def notes(verse_number,note):
	#print(verse_number,note)
	try:
		if note:
			if len(verse_number) < 4:
				'''Here it match the verse number to get first verse number'''
				findme = re.match(r"(\d+)(-\d+)?",verse_number,re.M|re.I)
				verses = findme.group(1)
				'''For creating '''
				if str(verse_number) == "intro":
					verses = verse_number
				elif len(verses) < 2:
					verses = '0' + verses
			else:
				verses = verse_number
		
			'''Replace • to #'''
			searchobj = re.sub(r'•','#',note)
			replace_obj = re.sub(r'-','\n',searchobj)

			''' Adding file extension '''
			filename = (verses + ".md")	

			if os.path.exists(filename):
				file = open(filename,'a')
				file.write("\n" + replace_obj)
			else:
				file = open(filename,'w')
				'''Writing into the new .md file'''
				file.write(replace_obj)
			''' To go back to previous directory'''
			os.chdir("..")				
			os.chdir("..")				
		else:
			os.chdir("..")				
			os.chdir("..")
	except:
		print("Error : ")
		os.chdir("..")				
		os.chdir("..")


'''Accessing the folder'''
os.chdir("tsv_files")

'''Fetching all .tsv files from the folder'''
files = glob.glob('*.tsv')
for filename in files:

	'''Opening and reading the .tsv file'''
	with open(filename,'r',encoding = 'utf-8') as tsvfile:
		reader = csv.reader(tsvfile, delimiter='\t')
		for row in reader:
			book = row[0]
			chapter = row[1]
			verse = row[2]
			hash_content = row[7]
			content = row[8]

			'''Aligning the content'''
			if hash_content:
				note = "# " + hash_content + "\n" + content
			else:
				note = content

			book_name(book)
			chapters_number(chapter)

			'''Using Regex for cleaning-up the unwanted contents'''
			#edited = re.sub(r"<br>"," ",note)
			edited_note = re.sub(r"(\[\[\w+\:[\/\w+\-]*\]\])","",note)
			hash_edit = re.sub(r"(#+)","\n\\1",edited_note)

			'''Calling the function for creating md files'''
			notes(verse, hash_edit)

			#print(book,chapter,verse,"# " + hash_content,content)