'''
	The script is for renaming the mp3 files in BC format and move it to new folder.
'''
import os
import glob
import re

'''Accesing the folder with the language name and version name (hin_irv)'''
lang_folders = glob.glob("*_*/")
new_folder = os.getcwd()

for lang_folder in lang_folders:
	os.chdir(lang_folder)

	'''Fetching the book folders'''
	book_folders = glob.glob("*/")
	x = 1
	for book_folder in book_folders:
		os.chdir(book_folder)
		path_folder = os.getcwd()
		bk_fldr_access = os.getcwd()

		'''Extracting folder name for creating new folder with extention "_audio" '''
		folder = re.sub(r"\/","",lang_folder)
		folder_name = folder + "_audio"

		bk_fldr_name = re.match(r"(\d+)\_?\-?(\d+)?",book_folder)
		if bk_fldr_name:
			book_name = bk_fldr_name.group(1)
		else:
			print(book_folder)

		'''Fetching all mp3 files'''
		mp3_files = glob.glob("*.mp3")
		
		for mp3_file in mp3_files:
			chap_mp3 = re.search(r"(\d+)(\.mp3)",mp3_file)

			'''Reanaming the mp3 from chapter number to BC format'''
			if chap_mp3:
				chap_mp3_file = chap_mp3.group(1)
				new_mp3 = folder.lower() + "_" + book_name.zfill(2) + chap_mp3_file.zfill(3) + ".mp3"
				print(mp3_file,new_mp3)
				os.chdir(new_folder)

				'''Creating new folder for moving the renamed mp3 files'''
				try:
					if not os.path.exists(folder_name):
						os.mkdir(folder_name)
						move_folder = os.getcwd()
						os.chdir(folder_name)
						
					else:
						os.chdir(folder_name)
						move_folder = os.getcwd()
	
				except OSError:
					print ('Error: Creating directory.' + folder_name)

				os.chdir(path_folder)

				'''The mp3 files into the new folder'''
				os.rename(bk_fldr_access + "/" + mp3_file, move_folder + "/" + new_mp3)
			
		
		'''Changing the directory'''
		os.chdir(path_folder)
		os.chdir("..")

	os.chdir("..")

