#!/usr/bin/python
# -*- coding: utf-8 -*-

import openpyxl
import re
import os
import sys
import glob
# import errno

mdfiles = glob.glob('en_ta_10/intro/**/*.md')
trmdfiles = glob.glob('tA_converted_md/intro/**/*.md')
outfolder = "or_ta"
if not os.path.exists(outfolder):
	os.mkdir(outfolder)
for i in trmdfiles:
	tr_firstdir = i.split('/')[1]
	for j in mdfiles:
		raw_firstdir = j.split('/')[1]
		if tr_firstdir == raw_firstdir:
			if not os.path.exists(outfolder + "/" + j.split('/')[1]):
				os.mkdir(outfolder + "/" + j.split('/')[1])
			tr_seconddir = i.split('/')[2]
			raw_seconddir = j.split('/')[2]
			if tr_seconddir == raw_seconddir:
				if not os.path.exists(outfolder + "/" + j.split('/')[1] + "/" + j.split('/')[2]):
					os.mkdir(outfolder + "/" + j.split('/')[1] + "/" + j.split('/')[2])
				tr_namemd = i.split('/')[3]
				raw_namemd = j.split('/')[3]
				if tr_namemd == raw_namemd:
					print ("en_ta/" + raw_firstdir + "/" + raw_seconddir + "/" + raw_namemd)
					with open(i) as trfile:
						links = []
						item = 0
						flag = 0
						outfile = open('%s/%s/%s/%s' %(outfolder, j.split('/')[1], j.split('/')[2], raw_namemd), "w")
						with open(j) as infile:
							k = 1
							flag = 0
							for inline in infile:
								searchobj = re.findall("(\(\s*?http\S*\/\)|\(\.*.\S*\.md\)|\[*rc:(\/*\w*-*\d*)*\]*)", inline)
								if searchobj:
									flag = 1
									for num in searchobj:
										links.append(num[0])
								k += 1

						for trline in trfile:
							pos = []
							outline = ""

							if flag == 1:
								searchobj = re.finditer("([\[P\d+])?(\])(.*)", trline)
								if searchobj:
									for num in searchobj:
										if re.search("openbiblestories.com", num.group(3)):
											print (trline)
										elif num.group(1) == None:
											pos.append(num.start())
										else:
											print (trline)
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
										outfile.write(outline)
								# findasterisk = re.search("\*{2}", outline)
								# if findasterisk:
								# 	arrasterisk = findasterisk.split("**")
								# 	outline += arrasterisk[0] + " **" + arrasterisk[1] + "** " + arrasterisk[2]
								# outline1 = re.sub("\*{2}\s(\w)", "**\1", outline)
								# outline2 = re.sub("\)\s__", ")__", outline1)
								# # outline3 = re.sub("__\s\[", "__[", outline2)
								# # outline4 = re.sub("\*__", "* __", outline3)

							if outline == "":
								outfile.write(trline)
							# 	# process1 = re.sub("#\s?#\s?", "## ", trline)
							# 	# process2 = re.sub("#\s?#\s?#\s?", "### ", process1)
							# 	# process3 = re.sub("#\s?#\s?#\s?#\s?", "#### ", process2)
							# 	# process4 = re.sub("#\s?#\s?#\s?#\s?#\s?", "##### ", process3)
							# 	if re.search("\*\S",process4):
							# 		process5 = re.sub("\*", "* ", process4)
							# 		outfile.write(process5)
							# 	# elif re.search("Strong's", process2):
							# 	# 	print " "
							# 	else:
							# 		outfile.write(process4)

						outfile.close()

print ('Counting Done !')
