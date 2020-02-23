#https://practice.geeksforgeeks.org/problems/longest-distinct-characters-in-string/0

no_of_chars=256
def ldc(s):
    curr_len=1
    max_len=1
    visited=[-1]*256
    prev_indx=0
    visited[ord(s[0])]=0
    
    for i in range(1,len(s)):
        prev_indx=visited[ord(s[i])]
        if prev_indx==-1 or i-curr_len>prev_indx:
            curr_len+=1
        else:
            if curr_len>max_len:
                max_len=curr_len
            curr_len=i-prev_indx
        visited[ord(s[i])]=i
    if curr_len>max_len:
        max_len=curr_len
    return max_len
    
    
for _ in range(int(input())):
    s=input()
    res=ldc(s)
    print(res)
