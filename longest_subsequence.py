arr=[100, 200, 1, 3, 2, 4,5]

maxi=0
res=set(arr)
for nums in res:
    if nums-1 not in res:
        count=1
        while nums+1 in res:
            count+=1
            nums+=1
        maxi=max(maxi,count)
    

print(maxi)