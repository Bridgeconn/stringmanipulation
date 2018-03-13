# Counting the number of words with alphabets less then 4 or 4

import csv

#string="hi i am vipin paul whats your name"
count=0
with open('word.csv','r') as file:
#file=open('word.csv','r')
#with file:
    reader = csv.reader(file)
    for row in reader:
        for words in row:
            #print("Its csv")
            #print(words)
            words=words.split(" ")
            for word in words:
            	if len(word)<=4:
            			count+=1
            			print(f"\n{word}")

#words=string.split(" ")
#print(len(word))
#print(words)

print("\nCount of words=",count)