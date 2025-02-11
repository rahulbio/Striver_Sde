arr=[9, -3, 3, -1, 6, -5]
k=0
maxi=float('-inf')
current=0
dict1={}
for i in range(len(arr)):
    current+=arr[i]

    if current==0:
        maxi=max(maxi,i+1)
    

    comple=current-k
    print(f"Comple is {comple} and current is {current}")
    if comple in dict1:
        maxi=max(maxi,i-dict1[comple])

    if current not in dict1:
        dict1[current]=i
    print(current,dict1[current])
print(maxi)
