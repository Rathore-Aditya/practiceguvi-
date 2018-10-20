n=input()
l=[]
if(n.isdigit()):
	a=1
	b=1
	n=int(n)
	l.append(a)
	l.append(b)
	for i in range(n-2):
		c=a+b
		l.append(c)
		a=b
		b=c
	for i in l:
		print(i,end=' ')	
else:
	print('Invalid Input')