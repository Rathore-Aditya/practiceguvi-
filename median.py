n=(input())
if(n.isdigit()):
	l=list(map(str,input().split()))
	for i in range(len(l)):
		if(l[i].isalpha()):
			print('Invalid Input')
			exit()		
	l.sort()
	if(int(n)%2!=0):
		m=(int(n)+1)//2
	else:
		m=(int(n)//2)+1
	print(l[m-1])	
else:
	print('Invalid Input')
	exit()					
