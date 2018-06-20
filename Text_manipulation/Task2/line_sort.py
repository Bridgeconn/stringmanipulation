'''
 Accepts a sequence of whitespace-separated words, 
 and show after removing duplicates and sort them as well.
'''

from collections import Counter

string = "hello world and practice makes perfect and hello world again"
input = []
input = string.split(" ")
input.sort()

for i in range(0, len(input)):
	input[i] = "".join(input[i])
unique = Counter(input)
line = " ".join(unique.keys())
print(line)