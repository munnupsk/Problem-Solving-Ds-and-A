#https://practice.geeksforgeeks.org/problems/majority-element/0/?track=md-arrays&batchId=144


#code
def findcandidate(li):
    max_index=0
    count=1
    for i in range(len(li)):
        if li[i]==li[max_index]:
            count+=1
        else:
            count-=1
        if count==0:
            max_index=i
            count=1
    return li[max_index]


def ismajority(li,can):
    count=0
    for i in range(len(li)):
        
        if li[i]==can:
            count+=1
    if count>len(li)//2:
        return can
    return '-1'


for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    can=findcandidate(li)
    print(ismajority(li,can))
