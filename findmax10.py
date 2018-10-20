l=list(input().split())
for i in l:
	if(i.isalpha() or len(l)>10):
		print('Invalid Input')
		exit()
print(max(l))