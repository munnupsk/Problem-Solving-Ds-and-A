
#https://practice.geeksforgeeks.org/problems/largest-number-possible/0

def res(d,s):
    r=[0]*d
    if s==0:
        if d==1:
            return 0
        else:
            return -1
    if s>9*d:
        return -1
    for i in range(d):
        if s>=9:
            r[i]=9
            s=s-9
        else:
            r[i]=s
            s=0
    return "".join(str(i) for i in r)
for i in range(int(input())):
    d,s=map(int,input().split())
    
    print(res(d,s))
            
