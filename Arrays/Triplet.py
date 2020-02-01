#https://practice.geeksforgeeks.org/problems/count-the-triplets/0

# solution 1
def triplets(arr, n):
    arr.sort()
    arr_set = set(arr)
    max_ele = arr[-1]
    res = 0
    for i in range(n-1):
        for j in range(i+1, n-1):
            s = arr[i]+arr[j]
            if s > max_ele:
                break
            if s in arr_set:
                res += 1
    print(res if res>0 else -1)




















#solution 2:

for i in range(int(input())):
     
    n=int(input())
    li=list(map(int,input().split()))
    maxi=0
    count=0
    for i in range(n):
        maxi=max(maxi,li[i])
    freq=[0 for i in range(maxi+1)]
    for i in range(n):
        freq[li[i]]+=1
    
    count+=(freq[0] * (freq[0] - 1) * (freq[0] - 2) // 6)
    
    for i in range(1,maxi+1):
        count+=(freq[0] * freq[i] *(freq[i] - 1) // 2)
    for i in range(1,(maxi+1)//2):
        count+=(freq[i] *(freq[i] - 1) // 2 * freq[2 * i])  
    for i in range(1, maxi + 1):  
        for j in range(i + 1, maxi - i + 1):  
            count += freq[i] * freq[j] * freq[i + j] 
    print(count)
  
        
    
