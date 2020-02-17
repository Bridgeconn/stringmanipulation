import re

bookMap = { 'Gen': 'GEN',
  'Exo': 'EXO',
  'Lev': 'LEV',
  'Num': 'NUM',
  'Deu': 'Deu',
  'Jos': 'JOS',
  'Jdg': 'JDG',
  'Rth': 'RUT',
  '1Sa': '1SA',
  '2Sa': '2SA',
  '1Ki': '1KI',
  '2Ki': '2KI',
  '1Ch': '1CH',
  '2Ch': '2CH',
  'Ezr': 'EZR',
  'Neh': 'NEH',
  'Est': 'EST',
  'Job': 'JOB',
  'Psa': 'PSA',
  'Pro': 'PRO',
  'Ecc': 'ECC',
  'Son': 'SNG',
  'Isa': 'ISA',
  'Jer': 'JER',
  'Lam': 'LAM',
  'Eze': 'EZK',
  'Dan': 'DAN',
  'Hos': 'HOS',
  'Joe': 'JOL',
  'Amo': 'AMO',
  'Oba': 'OBA',
  'Jon': 'JON',
  'Mic': 'MIC',
  'Nah': 'NAM',
  'Hab': 'HAB',
  'Zep': 'ZEP',
  'Hag': 'HAG',
  'Zec': 'ZEC',
  'Mal': 'MAL',
  'Mat': 'MAT',
  'Mar': 'MRK',
  'Luk': 'LUK',
  'Joh': 'JHN',
  'Act': 'ACT',
  'Rom': 'ROM',
  '1Co': '1CO',
  '2Co': '2CO',
  'Gal': 'GAL',
  'Eph': 'EPH',
  'Phi': 'PHP',
  'Col': 'COL',
  '1Th': '1TH',
  '2Th': '2TH',
  '1Ti': '1TI',
  '2Ti': '2TI',
  'Tit': 'TIT',
  'Phm': 'PHM',
  'Heb': 'HEB',
  'Jam': 'JAS',
  '1Pe': '1PE',
  '2Pe': '2PE',
  '1Jo': '1JN',
  '2Jo': '2JN',
  '3Jo': '3JN',
  'Jud': 'JUD',
  'Rev': 'REV' }

fopen = open('irvhin.txt', 'r')
alllines = fopen.readlines()
outfile = open('irvhin_csv.csv', 'w')

startBookIndex = 0
endBookIndex = 66

startChapterIndex = 66
endChapterIndex = 1255

startVerseIndex = 1255
endVerseIndex = len(alllines)

# bookIntros = []
# for i in range(startBookIndex, endBookIndex):
# 	bookintro = re.search(r'([1-9A-Za-z]{3})\t(.*)', alllines[i])
# 	if bookintro:
# 		bookIntros.append((bookintro.group(1),bookintro.group(2)))
# print(len(bookIntros))

# chapterIntros = []
# for j in range(startChapterIndex, endChapterIndex):
# 	chapterintro = re.search(r'([1-9A-Za-z]{3})\s?(\d+)\:\t(.*)', alllines[j])
# 	if chapterintro:
# 		chapterIntros.append((chapterintro.group(1), chapterintro.group(2), chapterintro.group(3)))
# print(len(chapterIntros))

VerseComm = []
for k in range(startVerseIndex, endVerseIndex):
  versecomm = re.search(r'([1-9A-Za-z]{3})\s?(\d+)\:(\d+(\-\d+)?(,\d+)?)\t(.*)', alllines[k])
  if versecomm:
    print (versecomm)
    VerseComm.append((versecomm.group(1), versecomm.group(2), versecomm.group(3), versecomm.group(6)))
  else:
    print (alllines[k])

print(len(VerseComm))


# for x in range(0, len(bookIntros)):
# 	outfile.write(bookMap[bookIntros[x][0]] + "\tfront\tintro\t" +  bookIntros[x][1] + "\n")
# 	for  y in range(0, len(chapterIntros)):
# 		if bookIntros[x][0] == chapterIntros[y][0]:
# 			outfile.write(bookMap[chapterIntros[y][0]] + "\t" + chapterIntros[y][1] + "\tintro\t\"" + chapterIntros[y][2] + "\"\n")
# 			for z in range(0, len(VerseComm)):
# 				if ((VerseComm[z][0] == chapterIntros[y][0]) and (chapterIntros[y][1] == VerseComm[z][1])):
# 					outfile.write(bookMap[VerseComm[z][0]] + "\t" + VerseComm[z][1] + "\t" + VerseComm[z][2] + "\t\"" + VerseComm[z][3] + "\"\n")

for z in range(0, len(VerseComm)):
  # if ((VerseComm[z][0] == chapterIntros[y][0]) and (chapterIntros[y][1] == VerseComm[z][1])):
  outfile.write(bookMap[VerseComm[z][0]] + "\t" + VerseComm[z][1] + "\t" + VerseComm[z][2] + "\t\"" + VerseComm[z][3] + "\"\n")
