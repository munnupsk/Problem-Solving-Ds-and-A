# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0

for i in range(int(input())): # No of tests cases
    n=int(input()) # length of the lists
    l=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    l2=list(enumerate(zip(l,l1)))
    l2.sort(key=lambda x:x[1][1])
    j=0
    print(l2[0][0]+1,end=" ")
    for i in range(1,len(l2)):
        if (l2[i][1][0]>=l2[j][1][1]):
            print(l2[i][0]+1,end=" ")
            j=i
    print()
