#https://practice.geeksforgeeks.org/problems/nuts-and-bolts-problem/0

def NB(nuts,bolts,n):
    priority={ '!':0, '#':1 ,'$':2 ,'%':3 ,'&':4 ,'*':5 ,'@':6, '^':7, '~':8 }
    temp=[0]*9
    arr=set(bolts)
    for i in nuts:
        if i in arr:
            temp[priority[i]]=i
    return " ".join(str(x) for x in temp if x!=0)

for _ in range(int(input())):
    n=int(input())
    nuts=list(input().split())
    bolts=list(input().split())
    res=NB(nuts,bolts,n)
    print(res)
    print(res)
    
