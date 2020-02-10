solution 1:



def kelement(arr1,arr2,m,n,k):
    i=0
    j=0
    
    while i<m and j<n:
        if arr1[i]>arr2[j]:
            k-=1
            
            if k==0:
                return arr2[j]
                
            j+=1
                
        elif arr1[1]<arr2[2]:
            k-=1
            if k==0:
                return arr1[i]
            i+=1
    
    if i<m:
        k-=1
        if k==0:
            return arr1[i]
        i+=1
    elif j<n:
        k-=1
        if k==0:
            return arr2[j]
        j+=1
        
    return -1
        

    
    # Time complexity O(m+n)
   
   
   #solution 2 :
   
   
   def ke(arr1,m,arr2,n,k):
    if k>(m+n) or k<1:
        return -1
    if m>n:
        return ke(arr2,n,arr1,m,k)
    
    if m==0:
        return arr2[k-1]
    
    if k==1:
        return min(arr1[0],arr2[0])
    
    i=min(m,k//2)
    j=min(n,k//2)
    
    if arr1[i-1]>arr2[j-1]:
        return ke(arr1,m,arr2[j:],n-j,k-j)
    else:
        return ke(arr1[i:],m-i,arr2,n,k-i)
        
    
    # Time complexity log(k) 
    
    
    
   
