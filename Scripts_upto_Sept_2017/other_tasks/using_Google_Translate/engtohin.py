import os
import glob
# import pdb
from google.cloud import translate
tc = translate.Client()
# translation = tc.translate("This is a boy", source_language="en", target_language="hi")
# print translation['translatedText']
folder = "Target"
if not os.path.exists(folder):
    os.mkdir(folder)

files = glob.glob('Source/*.md')
for file in files:
    try:
        f = open(file)
        name = file.split("/")[1]
        print name
        outfile = open('%s/%s' %(folder, name), "w")
        for line in f.readlines():
            translation = tc.translate(line, source_language="en", target_language="hi")
            outfile.write(translation['translatedText'].encode('utf-8') + "\n")
        outfile.close()
        f.close()
    except Exception as e:
        print(file + ": " + str(e))
        pass
