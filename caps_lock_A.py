# A
# caps lock 
# link https://codeforces.com/problemset/problem/131/A
str  = input()

if str.isupper():
	print(str.swapcase())
elif str[0].islower() and str[1:].isupper():
	print(str.swapcase())
elif str[0].islower() and len(str) == 1 :
	print(str.swapcase())
else :
	print(str)		

