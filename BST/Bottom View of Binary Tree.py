


def bottomView(root):
    
    arr = []
    
    # For tracking range of horizontal distance
    horiz_level_set = set()
    
    def traverseNodes(node, horiz_level, height):
        arr.append([node.data, horiz_level, height])
        horiz_level_set.add(horiz_level)
        if node.left:
            traverseNodes(node.left, horiz_level-1, height+1)
        if node.right:
            traverseNodes(node.right, horiz_level+1, height+1)
    
    traverseNodes(root, 0, 0)
    
    # Sort nodes by height
    arr.sort(key = lambda x: (x[2]))
    
    # print(arr)
    
    height_dict = defaultdict(lambda: -1)
    ans_dict = {}
    
    for e in arr:
        # '=' condition takes care of two nodes on same level having 0 horizontal distance
        if e[2] >= height_dict[e[1]]:
            height_dict[e[1]] = e[2]
            ans_dict[e[1]] = e[0]
    
    for level in sorted(list(horiz_level_set)):
        print(ans_dict[level], end = ' ')

