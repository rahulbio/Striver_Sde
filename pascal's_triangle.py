from math import comb

n=5
list2=[]
for i in range(n):
    list1=[]
    for j in range(i+1):
        list1.append(comb(i,j))
    list2.append(list1)
print(list2)

#ncr formula is the only formula required to kill pascal's triangle!