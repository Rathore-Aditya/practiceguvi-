n=input()
if(n.isdigit()):
	for i in range(1,6):
		print(int(n)*i,end=' ')
else:
	print('Invalid Input')		 