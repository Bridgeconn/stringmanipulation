import os
import glob
import docx
from docx import Document
import re


Source_files = glob.glob(os.getcwd() + "/Revised OBS TN - S3/TN URDU OBS-TN-S3/*.docx")
print(Source_files)
for fl in Source_files:
    dic = []
    document = Document(fl)
    tables = document.tables
    for table in tables:
        rows = table.rows
        for row in rows:
            try:
                folder_list = row.cells[0].text
                search_file_list = re.search(r'content.*?.*\.md', folder_list)
                if search_file_list:
                    in_fl_nme = folder_list.split('/')[-1].split('.')[0]
                    dic.append(in_fl_nme)
                else:
                    target_lan = row.cells[2].text
                    tar = re.match(r'Translation',target_lan)
                    if tar:
                        pass
                    else:
                        dic.append(target_lan)
            except:
                pass
    # print(dic)

    s_bkname = fl.split('/')[-1].split('.')[0].split(' ')[0]
    os.makedirs(os.getcwd() + '/' + 'outputfolder' + '/' + s_bkname)
    S_filePath = glob.glob(os.getcwd() + '/' + 'outputfolder' + '/' + s_bkname)
  
    for k in dic:
        find_num = re.match(r'\d+', k)
        if find_num:    
            file1 = k
            fn = open(S_filePath[0] +'/' + file1 +'.md', "w+")
        else:
            fa = open(S_filePath[0] +'/' + file1 + '.md', "a+")
            fa.write(k + "\n")
            fa.close()
print("completed")