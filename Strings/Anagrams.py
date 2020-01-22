#https://practice.geeksforgeeks.org/problems/anagram/0

def find(s1,s2):
    if len(s1)!=len(s2):
        return "NO"
        
    str1=sorted(s1)
    str2=sorted(s2)
    for i in range(len(s1)):
        if str1[i]!=str2[i]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    s1,s2=input().split()
    
    res=find(s1,s2)
    print(res)
    
    
            
        
        
        
