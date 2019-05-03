n,k=map(int,raw_input().split())
m=n//k
for i in range(m):
	if k**i==n:
		print("yes")
		break
	elif k**i>n:
		print("no")
		break
