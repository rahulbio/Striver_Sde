prices=[7,1,5,3,6,4]

maxi=float('-inf')
mini=float('inf')

for i in prices:
    mini=min(mini,i)
    maxi=max(maxi,i-mini)

print(maxi)