# Counting the number of words with alphabets less then 4 or 4


import csv

count = 0
with open('word.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:              #Reading the row
        for words in row:           #Reading the words in the row
            words = words.split(" ")
            for word in words:
            	if len(word) <= 4:
            			count += 1
            			print(f"\n{word}")

print("\nCount of words=",count)