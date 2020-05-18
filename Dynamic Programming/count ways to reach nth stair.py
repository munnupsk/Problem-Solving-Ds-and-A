


m=10**9
m=1000000007
fib=[0,1,2,3]
for i in range(4,10**6):
    a=fib[i-2]+fib[i-1]
    a%=m

    fib.append(a)

for _ in range(int(input())):
    print(fib[int(input())])
    
