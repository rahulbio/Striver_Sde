nums=[1,4,8,6]

def nextpermutation(nums):
    index=-1


    for i in range(len(nums)-2,-1,-1):
        if nums[i]<nums[i+1]:
            index=i
            break
    
    if index==-1:
        nums.reverse()
        return nums
        


    for j in range(len(nums)-1,index,-1):
        if nums[j]>nums[index]:
            nums[j],nums[index]=nums[index],nums[j]
            break
    
    nums[index+1:]=reversed(nums[index+1:])


    return nums


print(nextpermutation(nums))