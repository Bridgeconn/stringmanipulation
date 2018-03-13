# Put Question mark after the interrogative words and full stops 
# otherwise in a given sentence.


string = "Hi,How are you,What you want,its oki,Where are u going,mmm"
word = string.split(",")
z = 0
interrogatives = "what,What,where,Where,how,How,Why,why,Can,can"
a = interrogatives.split(",")
for x in word:
	y = x.split(" ")

	for i in a:
		if i == y[0]:
			x += '?'
			z = 1	

	if (z != 1):
		x += '.'
		z = 0
	print(x, sep = "\n")
	z = 0