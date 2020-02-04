#https://practice.geeksforgeeks.org/problems/non-repeating-element/0

for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    hash={}
    flag=1
    for i in range(n):
        if li[i] in hash:
            hash[li[i]]+=1
        else:
            hash[li[i]]=1
    for i in range(n):
        if li[i] in hash and hash[li[i]]==1:
            print(li[i])
            flag=0
            break
    if flag:
        print('0')
