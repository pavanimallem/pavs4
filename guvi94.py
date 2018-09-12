N,K=map(int,raw_input().split())
m=[int(x) for x in raw_input().split()]
for i in m:
	if i==K:
		print K
		break
	else:
		m.sort();
		if i>K:
			print i
			break
		
