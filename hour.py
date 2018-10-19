n=int(input())
if(n.isdigit()):
	h=n//60
	r=n%60
	print(h,r,end=' ')
else:
	print('Invalid Input')
	exit()		