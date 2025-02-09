a=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

for i in range(len(a)):
    for j in range(i+1,len(a[0])):
        a[i][j],a[j][i]=a[j][i],a[i][j]


for i in a:
    i[:]=i[::-1]

print(a)
