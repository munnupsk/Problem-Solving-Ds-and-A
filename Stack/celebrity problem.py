#  https://github.com/munnupsk/Problem-Solving-Ds-and-A/new/master/Stack


def getId(m,n):
    # code here
    stack=[]
    for i in range(n):
        stack.append(i)
    
    while len(stack)>1:
        s=stack.pop()
        p=stack.pop()
        if m[s][p]==0:
            stack.append(s)
        else:
            stack.append(p)
    
    x=stack.pop()
    
    for i in range(n):
        if i==x:
            continue
        if m[x][i]==1 or m[i][x]==0:
            return -1
    return x
            
