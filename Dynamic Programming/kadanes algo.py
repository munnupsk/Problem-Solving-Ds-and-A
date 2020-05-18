


t=int(input())
while t>0:
    n=int(input())
    
    li=list(map(int,input().split()))
    l=len(li)
    maxi=0
    max_at_end=0
    for i in range(0,l):
        
        max_at_end+=li[i]
        if max_at_end<0:
            max_at_end=0
        if maxi<max_at_end:
            maxi=max_at_end
    if maxi>0:
        print(maxi)
    else:
        print(max(li))
    t-=1
