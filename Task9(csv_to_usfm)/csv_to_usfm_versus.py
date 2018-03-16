# Make one .CSV file with tab separated and convert them into .usfm file.


import csv
import pandas as pd

book_name = []
chapter_num = []
ver = ""

# open a usfm file
file = open('1_JN.usfm','a')

# open and reading csv file
with open ('1_JN.csv', 'r', encoding = 'utf-8') as csv_file:
	creader = csv.reader(csv_file)

	for row in creader:
		if (row[0] != "\id "+row[0]):
			book = "\id "+row[0]
		chapter = "\c "+row[1]
		versu = "\\v "+row[2]
		versus = []
		versus += row[3:]
		ver = ''.join(versus)	# Converting list into string

		# Checks repeatation of book name and writing into file
		if (book != book_name):
			file.write(book+"\n")
			book_name = book

		# Checks repeatation of chapters and writing into file
		if (chapter != chapter_num):
			file.write(chapter+"\n")
			chapter_num = chapter

		file.write(versu+" "+ver+"\n")