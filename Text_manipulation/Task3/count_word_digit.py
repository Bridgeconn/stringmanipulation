'''
 Accepts a sentence which will have word and digit and calculate the count of letters and digits.
'''

string = input("Enter a combination of word and digit=")
print(string)
alphabet = 0
digit = 0

for i in string:
	if(i.isalpha()):
		alphabet += 1
	elif(i.isdigit()):
		digit += 1

print("Count of letters=", alphabet)
print("Count of digits=", digit)