arr=[1,3,4,2,2]

slow=arr[0]
fast=arr[0]

while True:
    slow=arr[slow]
    fast=arr[arr[fast]]
    print(f"Slow is {slow}")
    print(f"Fast is {fast}")
    if slow==fast:
        break


slow=arr[0]
while slow!=fast:
    slow=arr[slow]
    fast=arr[fast]

print(slow)