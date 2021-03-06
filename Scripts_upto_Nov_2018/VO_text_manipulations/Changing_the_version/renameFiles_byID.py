'''
Rename the usfm files with number and id in the directory based on the \id tag  
'''

import os
import re
import codecs
import pdb
import glob

''' Function for book code's contains Gen:01 to Mal:39 & Mat:41 to Rev:67'''
def getBookNum(bookCode):
    bk = {"GEN":"01", "EXO":"02", "LEV":"03", "NUM":"04", "DEU":"05", "JOS":"06", "JDG":"07", "RUT":"08", "1SA":"09", "2SA":"10", "1KI":"11", "2KI":"12", "1CH":"13", "2CH":"14", "EZR":"15", "NEH":"16", "EST":"17", "JOB":"18", "PSA":"19", "PRO":"20", "ECC":"21", "SNG":"22", "ISA":"23", "JER":"24", "LAM":"25", "EZK":"26", "DAN":"27", "HOS":"28", "JOL":"29", "AMO":"30", "OBA":"31", "JON":"32", "MIC":"33", "NAM":"34", "HAB":"35", "ZEP":"36", "HAG":"37", "ZEC":"38", "MAL":"39", "MAT":"41", "MRK":"42", "LUK":"43", "JHN":"44", "ACT":"45", "ROM":"46", "1CO":"47", "2CO":"48", "GAL":"49", "EPH":"50", "PHP":"51", "COL":"52", "1TH":"53", "2TH":"54", "1TI":"55", "2TI":"56", "TIT":"57", "PHM":"58", "HEB":"59", "JAS":"60", "1PE":"61", "2PE":"62", "1JN":"63", "2JN":"64", "3JN":"65", "JUD":"66", "REV":"67"}
    try:
        return(bk[bookCode])
    except KeyError:
        return("UNK***_" + bookCode)

''' Fetching all the folder's in directory'''
folders = glob.glob("*/")
print(folders)
for folder in folders:
    os.chdir(folder)
    files = os.listdir()

    for file in files:
        print(file)

        ''' Renames the files here '''
        try:
            if(file.split(".")[-1].lower()=="usfm" or file.split(".")[-1].lower()=="sfm"):
                f=codecs.open(file, mode='rb', encoding="utf-8")
                fc = f.read()
                f_id=re.search("\\\\id\s+(.{3})", fc, re.U)
                os.rename(file, getBookNum(f_id.group(1)) + "-" + str(f_id.group(1)) + ".usfm")
                f.close()
        except Exception as e:
            print(file, e.message)
            pass
    os.chdir("..")
