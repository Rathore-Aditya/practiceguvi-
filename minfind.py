n=int(input())
l=list(map(str,input().split()))
m=l[0]
for i in range(len(l)):
	if(l[i].isalpha()):
		print('Invalid Input')
		exit()		
	else:
		if(l[i]<m):
			m=l[i]
print(m)				
