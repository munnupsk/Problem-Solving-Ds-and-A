


for i in range(int(input())):
    n1,n2=map(int,input().split())
    
    s1=input()
    s2=input()
    
    
    m=len(s1)
    n=len(s2)
    
    li=[[0]*(n+1) for i in range(m+1)]
    
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                li[i][j]=0
                
            elif s1[i-1]==s2[j-1]:
                li[i][j]=li[i-1][j-1]+1
            else:
                li[i][j]=max(li[i-1][j],li[i][j-1])
    print(li[m][n])
    
