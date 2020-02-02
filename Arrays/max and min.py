
for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    maxi=-2147483648
    mini=2147483648
    for i in range(n):
        maxi=max(maxi,li[i])
        mini=min(mini,li[i])
    print("{} {}".format(mini,maxi))
