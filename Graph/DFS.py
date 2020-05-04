


def bfsutil(i,visited,g):
    visited[i]=True
    print(i,end=" ")
    for i in g[i]:
        if visited[i]==False:
            bfsutil(i,visited,g)
def dfs(g,N):
    '''
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the dfs of the graph from node 0, newline is given by driver code
    '''
    # code here
    visited=[False]*N
    
    bfsutil(0,visited,g)
