
#https://practice.geeksforgeeks.org/problems/longest-common-substring/0/?track=md-string&batchId=144




for _ in range(int(input())):
    l1,l2=map(int,input().split())
    s1=input()
    s2=input()
    res=[[0 for _ in range(l1+1)] for _ in range(l2+1)]
    max=0
    for i in range(1,l2+1):
        for j in range(1,l1+1):
            if s1[j-1]==s2[i-1]:
                res[i][j]=res[i-1][j-1]+1
                if max<res[i][j]:
                    max=res[i][j]
    print(max)
