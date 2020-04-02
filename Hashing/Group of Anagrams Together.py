#https://practice.geeksforgeeks.org/problems/k-anagrams-1/0



#code
from collections import defaultdict 
from operator import itemgetter
for _ in range(int(input())):
    n=int(input())
    li=input().split()
    l=[]
    hash=defaultdict(list)
    for i in li:
        hash["".join(sorted(i))].append(i)
    
    
    for i,v in sorted(hash.items(), key=itemgetter(1),reverse=True):
        print(len(v),end=" ")
    print()
        
        
    
