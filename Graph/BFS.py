


def bfs(g,N):
    '''
    can use queue module already imported
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the bfs of the graph from node 0, newline is given by driver code
    '''
    # code here
    visited=[False]*N
    queue=[]
    queue.append(0)
    visited[0]=True
    while len(queue):
        s=queue.pop(0)
        print(s,end=" ")
        for i in g[s]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
                
