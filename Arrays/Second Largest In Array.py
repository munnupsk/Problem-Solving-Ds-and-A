


for _ in range(int(input())):
    
    n=int(input())
    
    li=list(map(int,input().split()))
    
    first_max=-2147483648
    
    for i in range(n):
    
        first_max=max(first_max,li[i])
    
    second_max=-2147483648
    
    for i in range(n):
    
        if li[i]<first_max:
    
            second_max=max(second_max,li[i])
    
    print(second_max)
