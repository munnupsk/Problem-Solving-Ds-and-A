


def verticalOrder(root): 
    if root is None: 
        return
  
    # Create empty queue for level order traversal 
    queue = [] 
  
    # create a map to store nodes at a particular 
    # horizontal distance 
    m = {} 
  
    # map to store horizontal distance of nodes 
    hd_node = {} 
  
    # enqueue root 
    queue.append(root) 
    # store the horizontal distance of root as 0 
    hd_node[root] = 0
  
    m[0] = [root.data] 
  
    # loop will run while queue is not empty 
    while len(queue) > 0: 
  
        # dequeue node from queue 
        temp = queue.pop(0) 
  
        if temp.left: 
            # Enqueue left child 
            queue.append(temp.left) 
  
            # Store the horizontal distance of left node 
            # hd(left child) = hd(parent) -1 
            hd_node[temp.left] = hd_node[temp] - 1
            hd = hd_node[temp.left] 
  
            if m.get(hd) is None: 
                m[hd] = [] 
  
            m[hd].append(temp.left.data) 
  
        if temp.right: 
            # Enqueue right child 
            queue.append(temp.right) 
  
            # store the horizontal distance of right child 
            # hd(right child) = hd(parent) + 1 
            hd_node[temp.right] = hd_node[temp] + 1
            hd = hd_node[temp.right] 
  
            if m.get(hd) is None: 
                m[hd] = [] 
  
            m[hd].append(temp.right.data) 
  
    # Sort the map according to horizontal distance 
    sorted_m = collections.OrderedDict(sorted(m.items())) 
  
    # Traverse the sorted map and print nodes at each horizontal distance 
    for i in sorted_m.values(): 
        for j in i: 
            print(j, end=" ") 
