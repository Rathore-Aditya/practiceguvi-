a,b=input().split()
if(a.isdigit() and b.isdigit()):
	a=int(a)
	b=int(b)
	a=a^b
	b=a^b
	a=a^b
	print(a,b,end='')
else:
	print('Invalid Input')	