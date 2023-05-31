def isPlaindrome(s):
    temp=""
    for i in range(len(s)):
        if s[i].isalnum():
            temp+=s[i].lower()
    l=0
    r=len(temp)-1
    while(l<r):
        if temp[l]!=temp[r]:
            return False
        l+=1
        r-=1
    return True
    """l=0
    r=len(s)-1
    while(l<r):
        while l<r and not (s[l].isalnum()):
            l+=1
        while l<r and not (s[r].isalnum()):
            r-=1
        if s[l].lower()!=s[r].lower():
            return False
        l+=1
        r-=1
    return True"""
s = "A man, a plan, a canal: Panama"
print(isPlaindrome(s))
s = "race a car"
print(isPlaindrome(s))