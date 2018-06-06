''' 
Version Change : To change the ULB to IRV in all .json file's and folder's.
The modification is being done in the same file.
'''


import re
import os

'''Root folder name'''
path = "Bibles"

'''Fetching all files from folders and sub-folders'''
for root, sdirs, files in os.walk(path):
	for filename in files:
		file_path = os.path.join(root, filename)
		
		'''Fetching all json files'''
		if file_path.endswith('.json'):
			content=""
			json_file = open(file_path,'r+')
	
			for row in json_file:
				content += row

			'''Old file is being deleted after fetching data'''
			os.remove(file_path)

			'''Creating a new file with same name and path '''
			file = open(file_path,'w')

			'''Replacing the version'''
			ulb_edit = re.sub(r"ULB","IRV",content)
			irv_edit = ""
			irv_edit = re.sub(r"Unlocked Literal Bible","Indian Revised Version",ulb_edit)
			
			if irv_edit:
				print(irv_edit)
			else:
				irv_edit = content
			
			'''Writing into file'''
			file.write(irv_edit)
			file.close()

'''Fetch all folders'''
path = glob.glob("Bibles/*/*")

for folder in path:
	print(folder)
	
	''' Replaces the folder name'''
	os.rename(folder, folder.replace("ULB", "IRV"))