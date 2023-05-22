"""An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once."""
#Time Complexity - O(n)
#Space Complexity - O(n)
def isAnagram(s,t):
    dict1={}
    dict2={}
    if len(s)!=len(t):
        return False
    for each in s:
        if each in dict1.keys():
            dict1[each]+=1
        else:
            dict1[each]=1
    for each in t:
        if each in dict2.keys():
            dict2[each]+=1
        else:
            dict2[each]=1
    if dict1==dict2:
        return True

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))



