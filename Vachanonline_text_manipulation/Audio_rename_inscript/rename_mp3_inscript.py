'''
	The Script is written for renaming the .mp3 file for Inscript application.
	The renaming is done in ( 2 letter book standard name + chapter number )
'''
import os
import glob
import re

def new_name(name):
	''' Two letter standard book name's '''
	book = {"1":["GN"],"2":["EX"],"3":["LV"],"4":["NU"],"5":["DT"],"6":["JS"],"7":["JG"],"8":["RT"],
	"9":["S1"],"10":["S2"],"11":["K1"],"12":["K2"],"13":["R1"],"14":["R2"],"15":["ER"],"16":["NH"],
	"17":["ET"],"18":["JB"],"19":["PS"],"20":["PR"],"21":["EC"],"22":["SS"],"23":["IS"],"24":["JR"],
	"25":["LM"],"26":["EK"],"27":["DN"],"28":["HS"],"29":["JL"],"30":["AM"],"31":["OB"],"32":["JH"],
	"33":["MC"],"34":["NM"],"35":["HK"],"36":["ZP"],"37":["HG"],"38":["ZC"],"39":["ML"],"40":["MT"],
	"41":["MK"],"42":["LK"],"43":["JN"],"44":["AC"],"45":["RM"],"46":["C1"],"47":["C2"],"48":["GL"],
	"49":["EP"],"50":["PP"],"51":["CL"],"52":["H1"],"53":["H2"],"54":["T1"],"55":["T2"],"56":["TT"],
	"57":["PM"],"58":["HB"],"59":["JM"],"60":["P1"],"61":["P2"],"62":["J1"],"63":["J2"],"64":["J3"],
	"65":["JD"],"66":["RV"]}

	return book[name]

''' Open's the folder with (language_version) '''
lang_folders = glob.glob("*_*/")
new_folder = os.getcwd()

for lang_folder in lang_folders:
	os.chdir(lang_folder)

	'''fetching the book's folder '''
	book_folders = glob.glob("*/")
	x = 1
	for book_folder in book_folders:
		os.chdir(book_folder)
		path_folder = os.getcwd()

		bk_fldr_access = os.getcwd()
		folder = re.sub(r"\/","",lang_folder)
		folder_name = folder + "_audio"

		'''To extract the number of book'''
		bk_fldr_name = re.match(r"(\d+)\_?\-?(\d+)?",book_folder)
		if bk_fldr_name:
			book_name1 = bk_fldr_name.group(1)
			book_name = new_name(book_name1)

		else:
			print(book_folder)

		'''Fetching all mp3 files'''
		mp3_files = glob.glob("*.mp3")

		'''Reading each mp3 file'''
		for mp3_file in mp3_files:
			chap_mp3 = re.search(r"(\d+)(\.mp3)",mp3_file)

			if chap_mp3:
				chap_mp3_file = chap_mp3.group(1)

				'''Renaming the mp3 files'''
				new_mp3 = book_name[0] + chap_mp3_file.lstrip('0') + ".mp3"
			
				os.chdir(new_folder)

				''' Creating a new folder or using the folder ending with "_audio" '''
				try:
					if not os.path.exists(folder_name):
						os.mkdir(folder_name)
						move_folder = os.getcwd()
						os.chdir(folder_name)
						x = 0
					else:
						os.chdir(folder_name)
						move_folder = os.getcwd()
						x = 0
				except OSError:
					print ('Error: Creating directory.' + folder_name)

				os.chdir(path_folder)

				'''Moving the renamed mp3 files into new folder'''
				print(bk_fldr_access + "/" + mp3_file, move_folder + "/" + new_mp3)
				os.rename(bk_fldr_access + "/" + mp3_file, move_folder + "/" + new_mp3)
			
		'''Changing the directory'''
		print(book_folder)
		os.chdir(path_folder)
		os.chdir("..")

	os.chdir("..")