# Find all numbers which should divisible by 7 but are not a multiple of 5, 
# between 900 and 2000.


x=900
while x <= 2000:
	if( x%7 == 0 and x%5 != 0):
		print(x)
	x += 1 