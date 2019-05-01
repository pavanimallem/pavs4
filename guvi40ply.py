N = int(input())
count = 0
for i  in range(0,N+1):
	if i % 1 == 0 and i % 2  == 0:
		count =  count + 1
print(count)
