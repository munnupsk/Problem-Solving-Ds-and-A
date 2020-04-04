


def BS(li,low,high,k,searchFirst):
    result=-1
    while low<=high:
        mid=(low+high)//2
        if li[mid]==k:
            result=mid
            if searchFirst:
                high=mid-1
            else:
                low=mid+1
        elif li[mid]>k:
            high=mid-1
        else:
            low=mid+1
    return result

for _ in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    i=BS(li,0,n-1,k,True)
    if i ==-1 :
        print('-1')
    else:
        j=BS(li,i,n-1,k,False)
    
    
        print(j-i+1)
