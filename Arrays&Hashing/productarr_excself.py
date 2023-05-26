def productExceptSelf(nums):
    prod=1
    ans=[]
    count=nums.count(0)
    if count>1:
        prod=0
    else:
        for i in nums:
            if i!=0:
                prod*=i
    for i,val in enumerate(nums):
        if nums[i]==0:
            ans.append(prod)
        else:
            if count==1:
                ans.append(0)
            else:
                ans.append(int(prod/nums[i]))
    return ans
nums=[1,2,3,4]
print(productExceptSelf(nums))