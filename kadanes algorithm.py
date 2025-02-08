array=[-2,-3,-4,-5]

sum=0
maxi=array[0]

for i in range(len(array)):
    sum+=array[i]

    if sum>maxi:
        maxi=max(maxi,sum)
    
    if sum<0:
        sum=0
    

print(maxi)
