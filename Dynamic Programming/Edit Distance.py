


def minEdit(n1,n2,str1,str2):
    dp=[[0 for i in range(n1+1)] for i in range(n2+1)]
    
    for i in range(n2+1):
        for j in range(n1+1):
            
            #If first string is empty, only option is to 
            # insert all characters of second string 
            if i==0:
                dp[i][j]=j
             # If second string is empty, only option is to 
            # remove all characters of second string
                
            elif j==0:
                dp[i][j]=i
                
                
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str2[i-1] == str1[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
                
            
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
    return dp[n2][n1]
            

for i in range(int(input())):
    n1,n2=map(int,input().split())
    s1,s2=map(str,input().split())
    
    res=minEdit(n1,n2,s1,s2)
    
    print(res)
