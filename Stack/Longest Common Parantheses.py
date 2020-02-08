
#https://practice.geeksforgeeks.org/problems/longest-valid-parentheses/0

def findmax(s):
    stk=[]
    stk.append(-1)
    result=0
    for i in range(len(s)):
        if s[i]=='(':
            stk.append(i)
        else:
            stk.pop()
            if len(stk)!=0:
                result=max(result,i-stk[len(stk)-1])
            else:
                stk.append(i)
    return result
    
    
for _ in range(int(input())):
    s=input()
    s=[x for x in s]
    res=findmax(s)
    print(res)
