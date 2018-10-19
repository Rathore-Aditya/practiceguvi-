a,b=(input().split())
for i in range(int(a)+1,int(b)):
	j=i
	s=0
	while(j>0):
		r=j%10
		s+=r**3
		j=j//10
	if(s==i):
		print(i)
	else:
		pass
