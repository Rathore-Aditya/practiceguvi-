n=input()
w=('a','e','i','o','u','A','E','I','O','U')
if(n.isalpha()):
	if(n in w):
		print('Vowel')
	else:
		print('Consonant')	
else:
	print('Invalid')		