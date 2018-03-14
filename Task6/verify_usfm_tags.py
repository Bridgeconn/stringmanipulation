# To check the usfm tags and show the message to the user, 
# whether the file has a valid or invalid tag.


import re

file = open('3JN.usfm').read()
input = file.split("\n")
tags = "\id,\ide,\h,\\toc1,\\toc2,\\toc3,\mt,\s5,\c,\p,\\v,\\f,\\ft,\\fqa,\\fqb,\\f*,\q,\\b"
usfm_tags = tags.split(",")

for sentance in input:
	words=sentance.split(" ")
	for word in words:
		x = 1
#Using regular expression to match the first letter of word with "\"		
		matchobj = re.match(r'^\\', word)	
		if(matchobj):
			for tag in usfm_tags:
				if (word == tag):
					print("correct tag = ", word)
					x = 0
					break
			if (x > 0 ):
				print("Incorrect tag = ", word)