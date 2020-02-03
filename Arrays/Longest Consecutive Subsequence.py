#https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence/1

def findLongestConseqSubseq(arr, n):
    # code here
    arr.sort()
    count=1
    res=1
    for i in range(n-1):
        if arr[i+1]==arr[i]:
            continue
        if arr[i+1]==arr[i]+1:
            count+=1
            res=max(res,count)
        else:
            count=1
    return res
