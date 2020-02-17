import re
import os
import glob
import docx 
import csv
from docx.shared import Cm 
from docx import Document


# Tsv files
Source_files = glob.glob(os.getcwd() + "/Source/*.tsv")
print(Source_files)
# Docx files
Target_files = glob.glob(os.getcwd()+'/Target/tN_Level_1/tN Stage 1 Assamese/*.docx')
print(Target_files)
for t_fl in Target_files: # Docx files
    t_bookname = t_fl.split("/")[-1].split(".")[0]
    tl_content = []
    document = Document(t_fl)
    tables = document.tables
    for table in tables:
        tl_rows = table.rows
        for row in tl_rows:
            try:
                tl_book = row.cells[0].text
                tl_chapter = row.cells[1].text
                tl_verse = row.cells[2].text
                tl_occur = row.cells[4].text
                tl_content.append([tl_book, tl_chapter, tl_verse, tl_occur])
            except:
                pass
    tl_content.pop(0)  
    # # Tsv files
    
    tsvfile = open(Source_files[0],'r',encoding='utf-8')
    reader = csv.reader(tsvfile, delimiter='\t')
    with open(t_bookname + ".tsv", 'w', encoding='utf-8') as tsv_file:
        twriter = csv.writer(tsv_file, delimiter='\t')
        for rows in reader:
            combine_tl_ocr = ''
            eng_occur = rows[8]
            split_eng_ocr = eng_occur.split('\n')
            find_array_len = len(split_eng_ocr)
            array_count = find_array_len
            if (find_array_len > 1):
                subline_count = 0
                for sublines in split_eng_ocr:
                    if (sublines == ''):
                        print("emptyt")
                    elif subline_count == 0:
                        pop_tl_list = tl_content.pop(0)
                        combine_tl_ocr += pop_tl_list[3] + '\n'
                        subline_count += 1 
                    elif array_count == 1:
                        pop_tl_list = tl_content.pop(0)
                        book = pop_tl_list[0].split('\n')[0]
                        combine_tl_ocr += str(book) + "    " + pop_tl_list[1] + "    " + pop_tl_list[2] + "    " + pop_tl_list[3]
                    else:
                        pop_tl_list = tl_content.pop(0)
                        book = pop_tl_list[0].split('\n')[0]
                        combine_tl_ocr += str(book) + "    " + pop_tl_list[1] + "    " + pop_tl_list[2] + "    " + pop_tl_list[3] + "\n"
                    array_count -= 1        
                find_link_source = re.findall(r'(\[\[\w+\:[\/\w+\-]*\]\])', eng_occur)
                find_link_target = re.findall(r'@', combine_tl_ocr)
                edited_targetl = combine_tl_ocr
                dic1 = []
                if find_link_source:
                    for link in find_link_source:
                        if link == '':
                            pass
                        else:
                            dic1.append(link)
                    for k in dic1:
                        edited_targetl = edited_targetl.replace("@", k, 1)
                    rep_br = re.sub(r'\$', '<br>', edited_targetl)
                    twriter.writerow([rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rep_br.strip()])        

                    print(eng_occur)
                    print("------------------------------------------------------")
                    print(rep_br.strip())
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") 
                    print(" ")
                    print(" ")
                
                else:
                    rep_br = re.sub(r'\$', '<br>', combine_tl_ocr)
                    twriter.writerow([rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rep_br.strip()])

                    print(eng_occur)
                    print("------------------------------------------------------")
                    print(rep_br.strip())
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") 
                    print(" ")
                    print(" ")
           
            else:
                pop_tl_list = tl_content.pop(0)
                if pop_tl_list[3] == "Translation":
                    twriter.writerow([rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], "OccurrenceNote"])  

                    print(eng_occur)
                    print("------------------------------------------------------")
                    print("Occurance")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") 
                    print(" ")
                    print(" ")

                else:
                    find_link_source = re.findall(r'(\[\[\w+\:[\/\w+\-]*\]\])', eng_occur)
                    find_link_target = re.findall(r'@', pop_tl_list[3])
                    edited_targetl = pop_tl_list[3]
                    dic1 = []
                    if find_link_source:
                        for link in find_link_source:
                            if link == '':
                                pass
                            else:
                                dic1.append(link)
                        for k in dic1:
                            edited_targetl = edited_targetl.replace("@", k, 1)
                        rep_br = re.sub(r'\$', '<br>', edited_targetl)
                        twriter.writerow([rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rep_br.strip()]) 
                        
                        print(eng_occur)
                        print("------------------------------------------------------")
                        print(rep_br.strip())
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") 
                        print(" ")
                        print(" ")
                    
                    else:
                        rep_br = re.sub(r'\$', '<br>', pop_tl_list[3])
                        twriter.writerow([rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rep_br.strip()])

                        print(eng_occur)
                        print("------------------------------------------------------")
                        print(rep_br.strip())
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") 
                        print(" ")
                        print(" ")
            
            
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                # pop_tl_list = tl_content.pop(0)
                
            #         elif array_count == 1:
            #             pop_tl_list = tl_content.pop(0)
            #             book = pop_tl_list[0].split('\n')[0]
            #             combine_tl_ocr += str(book)+"    "+str(pop_tl_list[1]) +"    "+ str(pop_tl_list[2])+ "    "+str(pop_tl_list[3]) 
            #         elif subline_count == 0:
            #             pop_tl_list = tl_content.pop(0)
            #             combine_tl_ocr += pop_tl_list[3] +'\n'     
            #             subline_count += subline_count + 1
            #         else:
            #             pop_tl_list = tl_content.pop(0)
            #             book = pop_tl_list[0].split('\n')[0]
            #             combine_tl_ocr += str(book) + "    " + str(pop_tl_list[1]) + "    " + str(pop_tl_list[2]) + "    " + str(pop_tl_list[3]) + '\n'
            #         array_count -= 1
                # find_link_source = re.findall(r'(\[\[\w+\:[\/\w+\-]*\]\])', eng_occur)
                # find_link_target = re.findall(r'@', combine_tl_ocr)
                # edited_targetl = combine_tl_ocr
                # dic1 = []
                # if find_link_source:
                #     for link in find_link_source:
                #         if link == '':
                #             pass
                #         else:
                #             dic1.append(link)
                    # for k in dic1:
                    #     edited_targetl = edited_targetl.replace("@", k, 1)
                    # rep_br = re.sub(r'\$', '<br>', edited_targetl)
                    # twriter.writerow([rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rep_br]) 
                # else:
                #     rep_br = re.sub(r'\$', '<br>', pop_tl_list[3])
                #     twriter.writerow([rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rep_br])
            # else:
            #     pop_tl_list = tl_content.pop(0)
            #     if pop_tl_list[3] == "Translation":
            #         twriter.writerow([rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], "OccurrenceNote"])  
            #     else:
            #         find_link_source = re.findall(r'(\[\[\w+\:[\/\w+\-]*\]\])', eng_occur)
            #         find_link_target = re.findall(r'@', pop_tl_list[3])
            #         edited_targetl = pop_tl_list[3]
            #         dic1 = []
            #         if find_link_source:
            #             for link in find_link_source:
            #                 if link == '':
            #                     pass
            #                 else:
            #                     dic1.append(link)
            #             for k in dic1:
            #                 edited_targetl = edited_targetl.replace("@", k, 1)
            #             rep_br = re.sub(r'\$', '<br>', edited_targetl)
            #             twriter.writerow([rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rep_br]) 
            #         else:
            #             rep_br = re.sub(r'\$', '<br>', pop_tl_list[3])
            #             twriter.writerow([rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rep_br])
















# #                 # # CHECK LINk COUNT
    # #                 # if (len(find_link_source) == len(find_link_target)):
    # #                 #     pass
    # #                 # else:
    # #                 #     print(eng_occur)