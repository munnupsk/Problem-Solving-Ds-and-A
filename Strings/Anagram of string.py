
#https://practice.geeksforgeeks.org/problems/anagram-of-string/1

def remAnagram(str1,str2):
    
    #add code here
    count1=[0]*26
    count2=[0]*26
    res=0
    for i in range(len(str1)):
        count1[ord(str1[i])-ord('a')]+=1
    for i in range(len(str2)):
        count2[ord(str2[i])-ord('a')]+=1
    for i in range(26):
        res+=abs(count1[i]-count2[i])
    return res
    
