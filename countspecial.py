n=input()
c=0
for i in range(len(n)):
	if(not n[i].isdigit() and not n[i].isalpha() and not n[i]==' '):
		c+=1
print(c)		