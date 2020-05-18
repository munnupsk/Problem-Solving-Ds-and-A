



def permute(a,l,r,f):
    if l==r:
        f.append("".join(a))
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permute(a,l+1,r,f)
            a[l],a[i]=a[i],a[l]

for i in range(int(input())):
    s=input()
    s=list(s)
    f=[]
    permute(s,0,len(s)-1,f)
    f.sort()
    for i in f:
        print(i,end=" ")
    print()
