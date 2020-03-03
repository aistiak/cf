# ac 214 ms
# A 
# link : https://codeforces.com/problemset/problem/166/A

def foo(x):
	return (x[0],-x[1]) # if 1st vals are equal then inverse sort for 2nd val

n , k = list(map(int,input().strip().split(' ')))
hs = {}
lst = []
for i in range(n):
	tup = tuple(map(int,input().split(' ')))
	lst.append(tup)
	if tup not in hs :
		hs[tup]   = 1 
	else :
		hs[tup]  += 1
# sort the list 
lst = sorted(lst,key=foo,reverse=True)

print(hs[lst[k-1]])