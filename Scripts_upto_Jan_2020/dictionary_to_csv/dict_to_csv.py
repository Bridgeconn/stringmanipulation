import re
import glob

mdfiles = glob.glob('hindi_irv_dict/*.md')
mdfiles.sort()
outfile = open('irvhin_dict.csv', 'w')
hindi_dict = []
for i in mdfiles:
  print (i)
  with open(i) as fopen:
    filename = i.split('/')[1]
    englishword = filename.split('.md')[0]

    alllines = fopen.readlines()

    findword = re.search(r'#(.+)?[\,#]',alllines[0])
    hindiword = findword.group(1).strip()
    hindi_dict.append((hindiword, englishword, i))

hindi_dict.sort()
for j in range(0, len(hindi_dict)):
  outfile.write(hindi_dict[j][0][0] + "\t" + hindi_dict[j][0].split(",")[0] + "\t" + hindi_dict[j][1] + "\t" + hindi_dict[j][2] + "\n")
