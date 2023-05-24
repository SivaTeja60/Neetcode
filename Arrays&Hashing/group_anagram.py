import collections


def groupAnagram(strs):

    #List is not hashable so cant use as key in dictionary so we have to convert to tuple
    """sol={}
    for s in strs:
        count=[0]*26
        for each in s:
            count[ord(each)-ord('a')]+=1
        if tuple(count) in sol.keys():
            sol[tuple(count)].append(s)
        else:
            sol[tuple(count)]=[s]
    return sol.values()"""

    # By using collections.defaultdict(list) it avoids key error and adds the key value pair if it doesnt exist
    #     in the dictionary
    
    sol=collections.defaultdict(list)
    for s in strs:
            count=[0]*26
            for each in s:
                count[ord(each)-ord('a')]+=1
            sol[tuple(count)].append(s)
            
    return sol.values()



strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(strs))
