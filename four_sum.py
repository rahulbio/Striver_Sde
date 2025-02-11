arr=[1,0,-1,0,-2,2]
n=len(arr)
target=0
arr.sort()
result=[]
for i in range(n):
    if i>0 and arr[i]==arr[i-1]:
        continue
    for j in range(i+1,n):
        if j>i+1 and arr[j]==arr[j-1]:
            continue
        
        k=j+1
        l=n-1

        while(k<l):
            sum=arr[i]+arr[j]+arr[k]+arr[l]
            if sum==target:
                result.append([arr[i],arr[j],arr[k],arr[l]])
                k+=1
                l-=1
                while(k<l) and arr[k]==arr[k-1]:
                    k+=1
                
                while (k<l) and arr[l]==arr[l+1]:
                    l-=1
            
            elif sum>target:
                l=1
            
            elif sum<target:
                k+=1
print(result)



