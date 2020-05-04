


def DFSUtil(u, color,graph): 
        
    color[u] = "GRAY"
    for v in graph[u]: 
  
        if color[v] == "GRAY": 
            return True
  
        if color[v] == "WHITE" and DFSUtil(v, color,graph) == True: 
            return True
  
    color[u] = "BLACK"
    return False

def isCyclic(n, graph):
   
    color = ["WHITE"] *n
  
    for i in range(n): 
        if color[i] == "WHITE": 
            if DFSUtil(i, color,graph) == True: 
                return 1
    return 0
    

