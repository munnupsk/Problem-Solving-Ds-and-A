#https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1


def remove_duplicate(n, arr):
    #Code here
    j=0
    for i in range(n-1):
        if arr[i]!=arr[i+1]:
            arr[j]=arr[i]
            j+=1
    arr[j]=arr[n-1]
    return j+1
