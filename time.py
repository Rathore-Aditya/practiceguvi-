import math
a,b=(input().split())
c,d=(input().split())
if(int(a)<25 and int(c)<25 and int(b)<61 and int(d)<61):
	e=abs(int(b)-int(d))
	f=abs(int(a)-int(c))
	print(f,e,end=' ')
else:
	print('Invalid Input')
	 	
