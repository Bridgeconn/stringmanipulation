# Find and remove the words with length less than 3 and add them in new array


string = "Find and remove the words with less then add"
new = []
words = string.split(" ")
print(words)
for word in words:
	if(len(word) < 4):
		new.append(word)
		words.remove(word)

print(words)
print("---------------------")
print(new)