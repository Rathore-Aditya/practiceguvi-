n=input()
if(n.isalpha() or n.isalnum()):
	print('No')
	exit()
n=eval(n)	
if(isinstance(n,int) or isinstance(n,float)):
	print('Yes')
 	



 