a,b=input().split()
if(a.isdigit() and b.isdigit()):
	a,b=b,a
	print(a,b,end='')
else:
	print('Invalid Input')	