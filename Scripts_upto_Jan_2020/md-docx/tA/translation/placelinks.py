# -*- coding: utf-8 -*-
import re
import os
import glob
import docx 
from docx.shared import Cm 


S_files = glob.glob(os.getcwd() + "/en_ta-v11/")
# print(S_files)
Target_files = glob.glob(os.getcwd() + "/Stage2_tA_Converted/Telugu/**/**/*")
# print(Target_files)


for files in Target_files:
    f = files.split("/")[-3:]
    n = "/".join(f)
    # print(n)
    # opening Source file
    open_Sfile = S_files[0] + n
    try:
        open_f_S = open(open_Sfile, "r")
        source_content = open_f_S.read()
        findlinks = re.findall(r'(../.*?\.md)', source_content)
    except:
        print(n)
    
    if findlinks:
        # opening Target file
        try:
            open_f_T = open(files, "r+")
            target_content = open_f_T.read()
            edited_content = target_content
            for links in findlinks:
                edited_content = edited_content.replace("$", links, 1)
            open_f_T.seek(0)
            open_f_T.truncate()
            open_f_T.write(edited_content)
            open_f_T.close()
        except:
            print(n)
