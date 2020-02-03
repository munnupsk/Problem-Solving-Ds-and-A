#https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1

def printDuplicates(arr, n):
    # Code here
    flag=1
    for i in range(n):
        if arr[abs(arr[i])]>=0:
            arr[abs(arr[i])]=-arr[abs(arr[i])]
        else:
            print(abs(arr[i]),end=" ")
            flag=0
    if flag:
        print('-1')
    else:
        print()
