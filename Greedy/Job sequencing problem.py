#https://practice.geeksforgeeks.org/problems/job-sequencing-problem/0/


for _ in range(int(input())):
    l=int(input())
    li=list(map(int,input().split()))
    li1=[]
    j=0
    for _ in range(l):
        li1.append([li[j],li[j+1],li[j+2]])
        j+=3
    li1.sort(key=lambda x:x[2],reverse=True)
    res=[False]*l
    jobs=0
    sum=0
    for i in range(l):
        for j in range(min(l-1,li1[i][1]-1),-1,-1):
            if res[j] is False:
                res[j]=True
                jobs+=1
                sum+=li1[i][2]
                break
    print("{} {}".format(jobs,sum))
