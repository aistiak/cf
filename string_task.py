#A
#ac 
#link : https://codeforces.com/problemset/problem/118/A

str = input().lower()
vowels = ['a','e','i','o','u','y']
for v in str :
	if v not in vowels :
		print(".%s"%v,end="")

