#https://practice.geeksforgeeks.org/problems/return-two-prime-numbers/0/

import math
h=[False]*(100004)
primes=[]
def sieve():
    for i in range(2,int(math.sqrt(100004))+1):

        if h[i] is False:
            j = 2 * i
            while j<100004:
                h[j]= True
                j=j+i
                
    for j in range(2,100004):
        if h[j] is False:
            primes.append(j)
            
for _ in range(int(input())):
    n=int(input())
    sieve()
    i=0
    while (primes[i]<=(n//2)+1):
        diff=n-primes[i]
        if diff in primes:
            print("{} {}".format(primes[i],diff))
            break
        i+=1
            
        
    
