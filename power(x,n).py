x=4
n=3

if n<0:
    x=1/x
    n=-n

result=1

while (n>0):
    if (n%2!=0):
        result=result*x
    
    x*=x
    n//=2


print(result)
