#!/usr/bin/python
# -*- coding: utf-8 -*-

import openpyxl
import re
import os
import sys
import glob
import errno

mdfiles = glob.glob('TW/**/*.md')
trmdfiles = glob.glob('TW-Titus-MD/*.md')
outfolder = "TitusHindiTW"
if not os.path.exists(outfolder):
	os.mkdir(outfolder)
for i in trmdfiles:
	trnamemd = i.split('/')[1]
	for j in mdfiles:
		namemd = j.split('/')[2]
		if trnamemd == namemd:
			print namemd
			with open(i) as trfile:
				links = []
				item = 0
				strongnum = ""
				outfile = open('%s/%s' %(outfolder, namemd), "w")
				with open(j) as infile:
					for inline in infile:
						searchobj = re.findall("(\(\.\.(\/*\w*\d*)*\.md\)|\(rc:(\/*\w*-*\d*)*\))", inline)
						for num in searchobj:
							links.append(num[0])
						strongs = re.search("[HG]\d+\s?,?", inline)
						if strongs:
							strongnum = inline

				for trline in trfile:
					pos = []
					searchobj = re.finditer("\]", trline)
					outline = ""
					if searchobj:
						for num in searchobj:
							pos.append(num.start())
						if pos != []:
							n = 0
							start = 0
							end = pos[n] + 1
							for n in pos:
								if start != 0:
									end = n + 1
								newline = trline[start:end] + links[item]
								if trline[n+1]:
									start = end
								outline += newline
								item += 1
							outline += trline[end:]
						outline1 = re.sub("__\s?\*", "* __", outline)
						outline2 = re.sub("\)\s__", ")__", outline1)
						outline3 = re.sub("__\s\[", "__[", outline2)
						outline4 = re.sub("\*__", "* __", outline3)
						outfile.write(outline4)
					if outline == "":
						process1 = re.sub("# #", "##", trline)
						process2 = re.sub("## ##", "##", process1)
						if re.search("\*\S",process2):
							process3 = re.sub("\*", "* ", process2)
							outfile.write(process3)
						elif re.search("Strong's", process2):
							print " "
						else:
							outfile.write(process2)

				outfile.write(strongnum)
				outfile.close()
								
print 'Counting Done !'