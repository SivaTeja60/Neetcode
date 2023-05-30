def longestConsecutive(nums):
    #set doesnt support indexing so converting back to list
    nums=list(sorted(set(nums)))
    max_val=1
    temp=1
    if len(nums)==0:
        return 0
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]==1:
            temp+=1
        else:
            max_val=max(max_val,temp)
            temp=1
    return max(temp,max_val)

nums=[100,4,200,1,3,2]
print(longestConsecutive(nums))
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))