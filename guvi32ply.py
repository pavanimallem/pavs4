n,k=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
l=sorted(list)
if(k in l):
	print "Yes"
else:
	print "No"
