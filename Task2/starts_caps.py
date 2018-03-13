#Accepts sequence of lines, prints the sentence after making capitalized.


string = "first line,second line,last line"
words = []
words = string.split(",")

for word in words:
	print(word.capitalize(), sep = "\n")

print("\n---First Caps for all words---")

for word in words:
	print(word.title(), sep = "\n")