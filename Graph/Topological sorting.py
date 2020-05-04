


# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(graph) is a defaultict of type List
# n is no of edges

def toposortutil(v,visited,stack,graph):
    visited[v]==True
    for i in graph[v]:
        if visited[i]==False:
            toposortutil(i,visited,stack,graph)
    stack.insert(0,v)
def topoSort(n, graph):
    # Code here
    
    visited=[False]*n
    stack=[]
    for i in range(n):
        if visited[i]==False:
            toposortutil(i,visited,stack,graph)
    
        
    return stack

