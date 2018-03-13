# CSV file, add data in one column with heading "Name" and copy this created column in new column with heading "Copied name"

import csv
import copy

with open('copy.csv','r+', encoding='utf-8') as file:
	creader=csv.reader(file,delimiter=',')
	cwriter=csv.writer(file,delimiter=',')
	name=[]
	cname=[]
	#col=1
	rownumber = 1
	for row in creader:
		if rownumber == 1:
			cwriter.writerow(["Name", "Copied Name"])
		else:
			cwriter.writerow([row,row])
		rownumber = rownumber + 1

'''
		name+=row

	cname=copy.copy(name)
	#file.truncate()
	print(name)
	name.pop(0)
	print(cname)
	name.insert(0,"Copied name")
	print(name)

	for word in name:
		cwriter.writerow([''TEXTFILE.truncate(,word])'''