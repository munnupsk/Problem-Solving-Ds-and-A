
#https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0


for _ in range(int(input())):
    s=input()
    start=0
    maxlength=1
    for i in range(1,len(s)):
        #for longest even palin
        l=i-1
        r=i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1>maxlength:
                start=l
                maxlength=r-l+1
            r+=1
            l-=1
            
        # for odd palin "racecar"
        l=i-1
        r=i+1
        
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1>maxlength:
                start=l
                maxlength=r-l+1
            r+=1
            l-=1
            
    print(s[start:start+maxlength])
        
        
            
                
