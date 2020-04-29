



#code

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    j=0
    flag=0
    for i in range(1,n):
        if l[j]>=l[i]:
            flag=1
            break
    if  flag:
        print(0)
    else:
        print(1)
