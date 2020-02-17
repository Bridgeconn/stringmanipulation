# -*- coding: utf-8 -*-
import re
import os
import glob
import docx 
from docx.shared import Cm 


files = glob.glob(os.getcwd() + "/FW__tw_tQ/en_tw-master/en_tw/bible/*")

# print(files)
countw = {}
total_count = 0
for folder in files:
    wordcount = []
    bookname = folder.split('/')[-1]
    insidefolder = glob.glob(folder+"/*.md")
    for folder in insidefolder:
        f = open(folder, 'r')
        content = f.read()
        splitContent = content.split('\n')
        count = 1
        for lines in splitContent:
            process1 = re.sub(r"\(\s*?http\S*\/\)","",lines)
            process2 = re.sub(r"\(\.*.\S*\.md\)","",process1)
            process3 = re.sub(r"\(*\[*rc:(\/*\w*-*\d*)*\]*\)*","",process2)
            filterContent = re.sub(r"_", "_", process3)
            filtercc = re.sub(r"—", "-", filterContent)
            filterc = re.sub(r"’", "'", filtercc)
            filt = re.sub(r"…", "...", filterc)
            fil = re.sub(r"_", "-", filt)
            fi = re.sub(r"â€¦", "^ae!", fil)
            rem_numbers = re.sub(r'\d+','',fi)
            rem_punctuation = re.sub(r'[^\w\s]','',rem_numbers)
            rem_H = re.sub(r'H','',rem_punctuation)
            rem_G = re.sub(r'G','',rem_H)
            splitContent = rem_G.split(" ")
            for words in splitContent:
                if words == '':
                    pass
                else:
                    wordcount.append(words)
    wordLength = len(wordcount)
    total_count += wordLength
    countw[bookname] = wordLength
print(countw)
print(total_count)


