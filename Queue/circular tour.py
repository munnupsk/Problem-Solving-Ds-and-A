
#https://practice.geeksforgeeks.org/problems/circular-tour/1

def tour(lis, n):
    #Code here
    if n<=2:
        return 0
    curr_pet=lis[0][0]-lis[0][1]
    start=0
    end=1
    while end!=start or curr_pet<0:
        while curr_pet<0 and start!=end:
            curr_pet-=lis[start][0]-lis[start][1]
            start=(start+1)%n
            
            if start==0:
                return -1
        curr_pet+=lis[end][0]-lis[end][1]
        end=(end+1)%n
        
    return start
