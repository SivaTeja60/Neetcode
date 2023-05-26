def topKFrequent(nums,k):
    dict1={}
    ans=[]
    for each in nums:
        if each in dict1.keys():
            dict1[each]+=1
        else:
            dict1[each]=1
    dict1=dict(sorted(dict1.items(), key=lambda x:x[1],reverse=True))
    for i in dict1.keys():
        ans.append(i)
        if len(ans)==k:
            return ans
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))