''' 
To fetch the cross reference from the bible in BCV format.
Both the input and output files are in .txt and BCV format. 
'''

import os
import glob
import re

files = glob.glob("*.txt")
for file in files:

	''' extracting and Changing the file name's '''
	search_name = re.sub(r"(.*)\_(.*)\_(.*)\_(\d\.txt)","\\1_bib_\\3_\\4",file)
	search_cross = re.sub(r"(.*)\_(.*)\_(.*)\_(\d\.txt)","\\1_crs_\\3_\\4",file)

	''' Opening and fetching the content from bible '''
	file_obj = open(file,'r',encoding= "utf-8")
	file_read = file_obj.read()
	lines = file_read.split("\n")
	bible_content = ""
	cross_ref = ""

	for line in lines:
		''' Removing the cross-reference from the bible file '''
		remove_ref = re.sub(r"\(\s?(.*\s?\d+\s?\:\s?\d+\,?(.*)?(\d+)?)\s?\)","",line)
		bible_content += remove_ref + "\n"
		
		''' Extracting the cross-reference from the bible file '''
		fetch_ref = re.match(r"(\d+)(.*)\(\s?(.*\s?\d+\s?\:\s?\d+\,?(.*)?(\d+)?)\s?\)",line)
		if fetch_ref:
			'''
			if fetch_ref.group(4):
				cross_ref += fetch_ref.group(1) + "\t" + fetch_ref.group(3) + fetch_ref.group(4) + "\n"
				fetch_ref = ""
			else:
			'''
			cross_ref += fetch_ref.group(1) + "\t" + fetch_ref.group(3) + "\n"
			fetch_ref = ""


	'''Creating a "Bible" directory for storing the generated bible file without cross-ref'''
	try:
		if not os.path.exists("Bible"):
			os.mkdir("Bible")
			os.chdir("Bible")
			bible_path = os.getcwd()
			os.chdir("..")

		else:
			os.chdir("Bible")
			bible_path = os.getcwd()
			os.chdir("..")

	except OSError:
		print ('Error: No directory.' + "Bible")


	'''Creating a "Croos_ref" directory for storing the generated cross-reference data only'''
	try:
		if not os.path.exists("Croos_ref"):
			os.mkdir("Croos_ref")
			os.chdir("Croos_ref")
			Croos_ref_path = os.getcwd()
			os.chdir("..")

		else:
			os.chdir("Croos_refe")
			Croos_ref_path = os.getcwd()
			os.chdir("..")

	except OSError:
		print ('Error: No directory.' + "Croos_ref")


	''' Saving the content in BCV format after removing the cross-reference '''
	bib_file = open(bible_path + "/" + search_name,'w',encoding= "utf-8")
	bib_file.write(bible_content)
	bib_file.close()

	''' Creating a new file for saving the cross-reference in BCV format '''
	cross_file = open(Croos_ref_path + "/" + search_cross , 'w', encoding = "utf-8")
	cross_file.write(cross_ref)
	cross_file.close()