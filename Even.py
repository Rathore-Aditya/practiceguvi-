n=input()
if(n.isdigit()):
	n=int(n)
	if(not n%2):
		print('Even')
	else:
		print('Odd')
else:
	print('Invalid')			