#Accepts comma-separated words as input and prints the words
#in a comma separated sequence after sorting them alphabetically.


string = "hello,without,maybe,thanks,apple"
word = string.split(",")
words = []
print(word)
word.sort()
print("After sorting \n", word, sep = ",")