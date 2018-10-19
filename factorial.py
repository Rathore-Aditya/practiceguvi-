n=input()
if(n.isdigit()):
	f=1
	for i in range(1,int(n)+1):
		f=f*i

	print(f)
else:
	print('Invalid')


