a,b=input().split()
l=[]
s=0
l=list(map(int,input().split()))
 
for j in range(int(b)):
	s+=l[j]
print(s)	