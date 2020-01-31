#https://practice.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1/?track=md-arrays&batchId=144


def maxLen(n, lis):
    #code here
    for i in range(n):
        if lis[i]==0:
            lis[i]=-1
    
    sum=0
    max=0
    hash={}
    for i in range(n):
        
        sum+=lis[i]
        if sum==0:#special case if ex -1,1  res=2 here sum=0
            max=i+1
        if sum in hash:
            if max<i-hash[sum]:
                max=i-hash[sum]
            
        
        else:
            hash[sum]=i
    return max
