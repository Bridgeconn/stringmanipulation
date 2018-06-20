'''
 Read one file with multi-sentences then find add the word which starts with vowel character.
'''

doc = open('vowel.txt', 'r')
doc_read = doc.read()
print(doc_read)
string = doc_read.split()
print("---Vowel words in file--- ")

for i in string:
	for x in i[0]:
		if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
			print(i)