#https://practice.geeksforgeeks.org/problems/anagram-palindrome/0

def polin(s):
    arr=[0]*256
    for i in s:
        arr[ord(i)]+=1
    odd=0
    for i in range(256):
        if arr[i]==1:
            odd+=1
        elif arr[i]%2!=0:
            odd+=1
        if odd>1:
            return "No"
    return "Yes"
    
    
    
for _ in range(int(input())):
    s=input()
    res=polin(s)
    print(res)
