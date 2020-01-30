 #https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form-set-2-o1-extra-space/
 
def rearrange(arr, n): 
  
 
    max_idx = n - 1
    min_idx = 0
  
   
    max_elem = arr[n-1] + 1
  
     
    for i in range(0, n) : 
  
        # At even index : we have to put maximum element 
        if i % 2 == 0 : 
            arr[i] += (arr[max_idx] % max_elem ) * max_elem 
            max_idx -= 1
  
        # At odd index : we have to put minimum element 
        else : 
            arr[i] += (arr[min_idx] % max_elem ) * max_elem 
            min_idx += 1
  

    for i in range(0, n) : 
        arr[i] = arr[i] / max_elem 
