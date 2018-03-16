# Make one .usfm file and convert into .csv file by removing the tags.
# From a single book

import csv
import re
import pandas as pd

book_name = []
chapter = ""
file = open('1_JN.usfm').read()
file = file.split("\n")

with open ('JN1.csv', 'w', encoding = 'utf-8') as csv_file:
	cwriter = csv.writer(csv_file,dialect='excel')

	# Loading the content
	for words in file:
		matchobj = re.match(r'(\\..?) (.*)', words, re.M|re.I) # RE for finding the book name
		if matchobj:
			name = matchobj.group(2)
			book_name += list(name.split("\n"))
	book = book_name[0]	#Selecting the name once

	# Reading the file again for spliting the chapter and versus 
	for word in file:
		# Grouping the verse number and versus
		searchobj = re.match(r'(\\..?)(\d )(.*)', word, re.M|re.I)
		chapobj = re.match(r'(\\c) (\d)', word, re.M|re.I)
		if chapobj:
			chapter = chapobj.group(2)
			
		if searchobj:
			verse_number = searchobj.group(2)
			versus = searchobj.group(3)
			# Write into csv file column vise
			cwriter.writerow([book,chapter,verse_number,versus]);