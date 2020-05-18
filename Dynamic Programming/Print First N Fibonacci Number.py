


for i in range(int(input())):
    n=int(input())
  
    f1=0
    f2=1
    print(f2,end=" ")
    for i in range(n-1):
        print(f1+f2,end=" ")
        next=f1+f2
        f1=f2
        f2=next
    print()
