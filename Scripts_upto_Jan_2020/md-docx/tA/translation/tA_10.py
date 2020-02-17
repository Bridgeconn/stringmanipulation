import os
import glob
import docx
from docx import Document
import re

# mdSource = glob.glob(os.getcwd() + "/en_ta_10/intro/*")
# print(mdSource)

docxFiles = glob.glob(os.getcwd() + "/S2_tA_mal_ben_tel/Telugu/intro/*.docx")
print(docxFiles)


for fl in docxFiles:
    # sub_list = ["title","sub-title","01"]
    fileName = fl.split('/')[-1].split('.')[0]
    print(fileName)
    os.makedirs(os.getcwd() + '/' + 'newfolder' + '/' + fileName)
    S_filePath = glob.glob(os.getcwd() + '/' + 'newfolder' + '/' + fileName)
    document = Document(fl)
    tables = document.tables
    for table in tables:
        rows = table.rows
        for row in rows:
            try:
                content = row.cells[0].text
                # print(content)
                search_filename = re.search(r'\w+\/.*?\/.*?.md', content)
                if search_filename:
                    title_name = search_filename.group(0)
                    split_tname = title_name.split('/')[-1].strip()
                    f = open(S_filePath[0] + "/" + split_tname, "w+")
                    f.close()
            except:
                pass
            try:
                content1 = row.cells[2].text
                search_title = re.search(r'\w+\/.*?\/.*?.md', content1)
                # search = re.match(r'\#', content1)
                if content1 == "Translation":
                    pass
                elif search_title:
                    pass
                # elif search:
                #     f = open(S_filePath[0] + "/" + split_tname + ".md", "a")
                #     f.write("\n")
                #     f.write(content1 + "\n")
                #     f.write("\n")
                #     f.close()
                else:
                    f = open(S_filePath[0] + "/" + split_tname, "a")
                    f.write(content1 + "\n")
                    f.close()
            except:
                pass




















