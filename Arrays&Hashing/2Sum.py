def twoSum(nums,target):

    #Time complexity - O(n)
    prevNum={}
    for i,n in enumerate(nums):
        if target-n in prevNum:
            return [i,prevNum[target-n]]
        prevNum[n]=i

nums=[2,7,11,15]
target=13
print(twoSum(nums,target))
