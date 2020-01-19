#https://practice.geeksforgeeks.org/problems/primes-sum/0

# give a number N,check whether sum of two primes is equal to N

# Every even integer greater than 2 can be expressed as the sum of two primes.

import math
def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
        
for _ in range(int(input())):
    n=int(input())
    if n<=3:
        print("No")
    elif n%2==0:
        print("Yes")
    else:
        if isprime(n-2):
            print("Yes")
        else:
            print("No")
            
            
# also check   https://www.geeksforgeeks.org/check-if-a-prime-number-can-be-expressed-as-sum-of-two-prime-numbers/
    
            
    
    
    
