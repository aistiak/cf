# A 
# ac 
# link : https://codeforces.com/problemset/problem/1303/A
t_c = int(input())
result = []
for v in range(t_c):
	bn    = input()
	left  = bn.find('1')
	right = bn.rfind('1') + 1
	result.append(str(bn[left:right].count('0')))

print('\n'.join(result))	
