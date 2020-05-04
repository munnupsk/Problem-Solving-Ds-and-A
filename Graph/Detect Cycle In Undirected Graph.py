


def isCyclicUtil(v,visited,parent,graph): 
    visited[v]= True
    for i in graph[v]: 
     
        if  visited[i]==False :  
            if(isCyclicUtil(i,visited,v,graph)): 
                return True
          
        elif  parent!=i: 
            return True
          
    return False
def isCyclic(g,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    # code here
    visited =[False]*n 
        # Call the recursive helper function to detect cycle in different 
        #DFS trees 
    for i in range(n): 
        if visited[i] ==False: #Don't recur for u if it is already visited 
            if(isCyclicUtil(i,visited,-1,g))== True: 
                return 1
          
    return 0
