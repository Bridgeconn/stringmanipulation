import json
import codecs
import pdb
import csv
import os
import sys
import glob
import errno

files = glob.glob('**/*.json')
for name in files:
    folder_name = name.split('/')[0]
    file_namewx = name.split('/')[1]
    file_name = file_namewx.split('.')[0]

    if not os.path.exists('%s/CSV' %(folder_name)):
                        os.mkdir("%s/CSV" %(folder_name))

    print "Parsing file: " + name

    f = codecs.open(name, mode="r", encoding="utf-8")
    data=json.loads(f.read())

    # open csv file for writing
    lexicon_data = open('%s/CSV/%s.csv' %(folder_name, file_name), 'w')
    csvwriter = csv.DictWriter(lexicon_data, fieldnames = ["Key", "Pronunciation", "Lexeme", "Transliteration", "Definition", "StrongsNumber"], delimiter ='\t')
    csvwriter.writeheader()

    # create the csv writer object
    csvwriter = csv.writer(lexicon_data, delimiter ='\t')


    for item in data.items():
        key = item[0].encode('utf-8')
        if item[1]['pronunciation'] != None:
            pron = item[1]['pronunciation'].encode('utf-8')
        else:
            pron = ""

        if item[1]['unicode'] != None:
            lex = item[1]['unicode'].encode('utf-8')
        else:
            lex = ""

        if item[1]['translit'] != None:
            trans = item[1]['translit'].encode('utf-8')
        else:
            trans = ""

        if item[1]['definition'] != None:
            define = item[1]['definition'].encode('utf-8')
            define = " ".join(define.split())
        else:
            define = ""

        stro = item[1]['strongs_number'].encode('utf-8')

        csvwriter.writerow([key, pron, lex, trans, define, stro])


    # close the csv file
    lexicon_data.close()
    print "Conversion done!"
