arr1=[2,2,1,1,1,2,2]


candidate,count=None,0


for num in arr1:
    if count==0:
        candidate=num
        count=1
    elif candidate==num:
        count+=1
    
    else:
        count-=1


print(candidate)

arr2=[11,33,33,11,33,11]
candidate1,candidate2,count1,count2=None,None,0,0

for nu in arr2:
    if count1==0 and candidate2!=nu:
        candidate1=nu
        count1=1
    elif count2==0 and candidate1!=nu:
        candidate2=nu
        count2=1
    elif candidate1==nu:
        count1+=1
    elif candidate2==nu:
        count2+=1
    else:
        count1-=1
        count2-=1


print(candidate1,candidate2)