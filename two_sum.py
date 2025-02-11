array=[2,6,5,8,11]
target=14


dict1={}


def twosum(array):
    for i,num in enumerate(array):
        complement=target-num
        if complement in dict1:
            return [dict1[complement],i]
        dict1[num]=i
    
    return [-1,-1]

print(twosum(array))