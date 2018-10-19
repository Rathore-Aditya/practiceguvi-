a,b=(input().split())
for i in range(int(a)+1,int(b)):
	n=i
	f=0
	for j in range(2,int(n**0.5)+1):
		if(n%j==0):
			f=1
			break
	if(f==0):
		print(n,end=' ')
	else:
		continue			
