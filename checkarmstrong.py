n=(input())
s=0
if(n.isdigit()):
	n=int(n)
	j=n
	while(n>0):
		r=n%10
		s+=r**3
		n=n//10
	if(j==s):
		print('YES')
	else:
		print('No')
else:
	print('Invalid')		