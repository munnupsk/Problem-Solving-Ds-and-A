
#https://practice.geeksforgeeks.org/problems/check-if-two-strings-are-k-anagrams-or-not/1

def areKAnagrams(str1, str2, k):
    # Code here
    if len(str1)!=len(str2):
        return 0
    hash=[0]*26
    for i in str1:
        hash[ord(i)-ord('a')]+=1
    count=0
    for i in str2:
        if hash[ord(i)-ord('a')]>=1:
            hash[ord(i)-ord('a')]-=1
        else:
            count+=1
        if count>k:
            return 0
    return 1
            
