n=(input())
if(n.isdigit()):
	l=list(map(str,input().split()))
	for i in range(len(l)):
		if(l[i].isalpha()):
			print('Invalid Input')
			exit()		
	l.sort()
	for i in l:
		print(i,end=' ')
else:
	print('Invalid Input')
	exit()					
