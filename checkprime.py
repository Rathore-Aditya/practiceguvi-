n=int(input())
f=0
for i in range(2,n//2):
	if(n%i==0):
		f=1
		break
if(f==0):
	print('YES')
else:
	print('NO')			
