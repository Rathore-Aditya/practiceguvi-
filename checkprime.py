n=(input())
f=0
if(n.isdigit()):
	for i in range(2,int(n)//2):
		if(int(n)%i==0):
			f=1
			break
else:
	print('Invalid')
	exit()			
if(f==0):
	print('YES')
else:
	print('NO')			
