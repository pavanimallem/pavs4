x=int(raw_input())
mul=1
while(x!=0):
  digit=x%10
  mul=mul*digit
  x=x/10
print mul  
