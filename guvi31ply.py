string=raw_input()
a=0
b=0
length=len(string)
for i in range(0,length):
	if(string[i]==')'):
		a+=1
	elif(string[i]=='('):
		b+=1
if(a-b==0):
	print"yes"
else:
	print"no"
