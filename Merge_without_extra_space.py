nums1=[1,4,8,10]
nums2=[2,3,9]
n=4
m=3

i=n-1
j=0


while(i>=0 and j<m):
    if(nums1[i]>nums2[j]):
        nums1[i],nums2[j]=nums2[j],nums1[i]
        i-=1
        j+=1
    else:
        break

nums1.sort()
nums2.sort()

print([nums1,nums2])