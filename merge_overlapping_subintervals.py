arr=[[1,4],[4,5]]

arr.sort()


ans=[arr[0]]


for i in range(len(arr)):
    if(arr[i][0]<=ans[-1][-1]):
        ans[-1][-1]=max(ans[-1][-1],arr[i][1])
    
    else:
        ans.append(arr[i])

print(ans)