#https://practice.geeksforgeeks.org/problems/non-repeating-character/0

for _ in range(int(input())):
    n=int(input())
    li=input()
    hash={}
    flag=1
    for i in li:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
        
    for i in li:
        if hash[i]==1:
            flag=0
            print(i)
            break
    if flag:
        print('-1')
