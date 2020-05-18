


def printPattern(n,m,flag):
    print(m,end=" ")
    
    if n==m and not flag:
        return 
    
    if flag:
        if m-5>0:
            printPattern(n,m-5,True)
        else:
            printPattern(n,m-5,False)
    else:
        printPattern(n,m+5,False)
        
for i in range(int(input())):
    m=int(input())
    printPattern(m,m,True)
    print()
