import os
import glob
import docx
from docx import Document
import re


Source_files = glob.glob(os.getcwd() + "/intro/*")
for fl in Source_files:
    inside_fl_folder = glob.glob(fl+"/*")
    S_folderName = fl.split('/')[-1]
    os.makedirs(os.getcwd() + '/' + 'outputfolder' + '/' + S_folderName)
    for md in inside_fl_folder:
        in_fileName = md.split('/')[-1].split(".")[0]
        S_filePath = glob.glob(os.getcwd()+ '/' + 'outputfolder' + '/' + S_folderName)
        # print(md)
        document = Document(md)
        tables = document.tables
        with open(S_filePath[0] + "/" + in_fileName + ".md", "w+") as md:
            for table in tables:
                rows = table.rows
                count1 = 0
                for row in rows:
                    try:
                        folder_list = row.cells[2].text
                        print(folder_list)
                        search = re.match(r'\#', folder_list)
                        if search:
                            md.write("\n")
                            md.write(folder_list + "\n")
                            md.write("\n")
                        elif count1 < 2:
                            print("next")
                            count1 += 1
                        else:
                            md.write(folder_list + "\n")
                            # md.write("\n")
                    except:
                        pass