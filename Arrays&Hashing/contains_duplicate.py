def containsDuplicate(num):
    """ #Time Complexity - O(n^2)
    #Space Complexity - O(n)
    temp=[]
    for i in num:
        if i in temp:
            return True
        else:
            temp.append(i)
    return False """

    #Time Complexity - O(n)
    #Space Complexity - O(1)
    nums.sort()
    for i in range(0,len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False
    

nums = [1,2,3]
print(containsDuplicate(nums))
