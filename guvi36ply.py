N,K=map(str,raw_input().split(" "))
count=0
for i in range(0,len(N)):
	if N[i]==K:
		count=count+1
print(count)	
