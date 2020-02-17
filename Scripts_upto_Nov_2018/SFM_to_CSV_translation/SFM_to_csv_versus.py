'''
 Convert .sfm into .csv file by removing the tags for multiple files.
'''

import csv
import re
import glob
import os
import pandas as pd

chapter = ""
files = glob.glob("*.SFM")

'''Reading the sfm file one by one'''
for sfm_file in files:
	file_obj = open(sfm_file).read()
	file = file_obj.split("\n")

	'''Loading the content'''
	for words in file:
		''' Regex is for finding the book name'''
		matchobj = re.match(r'(\\id) (...)', words, re.M|re.I)
		if matchobj:
			book = matchobj.group(2)
	print(book)

	'''Creating a new directory if not available'''
	try:
		if not os.path.exists("csv"):
			os.mkdir("csv")
			os.chdir("csv")
		else:
			os.chdir("csv")
	except OSError:
		print ('Error: Creating directory.' + "csv")

	'''Creating a csv file with book name'''
	with open (book + '.csv', 'w', encoding = 'utf-8') as csv_file:
		cwriter = csv.writer(csv_file,dialect='excel')
		
		cwriter.writerow(["Book","Chapter","Verse","Versus"]);
		
		''' Reading the file again for spliting the chapter and versus''' 
		for word in file:
			print(word)
			
			'''Grouping the verse number and versus'''
			searchobj = re.match(r'(\\v )(\d+ )(.*)', word, re.M|re.I)
			chapobj = re.match(r'(\\c) (\d+)', word, re.M|re.I)
			if chapobj:
				chapter = chapobj.group(2)
				
			if searchobj:
				verse_number = searchobj.group(2)
				versus_tags = searchobj.group(3)
				versus_edit = re.sub(r"((\\add) ?\*?)","",versus_tags)
				versus_sub = re.sub(r"([\►\◄])","",versus_edit)
				versus = re.sub(r"\\s\d+(.*)","",versus_sub)
				
				''' Writing the edited content into csv file column vise'''
				cwriter.writerow([book,chapter,verse_number,versus]);
				print(book,chapter,verse_number,versus)
	os.chdir("..")