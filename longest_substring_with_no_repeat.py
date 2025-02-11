a="bbbb"

seen=set()


left=0
max_length=0
for right in range(len(a)):
    while a[right] in seen:
        seen.remove(a[left])
        left+=1
    
    seen.add(a[right])
    max_length=max(max_length,right-left+1)

print(max_length)
