
#https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream/0


from queue import Queue
def firstnonrepeating(Str): 
    MAX_CHAR=26
    q = Queue() 
    charCount = [0] * MAX_CHAR  
      
    # traverse whole Stream 
    for i in range(len(Str)): 
  
        # push each character in queue  
        q.put(Str[i])  
  
        # increment the frequency count  
        charCount[ord(Str[i]) - 
                  ord('a')] += 1
  
        # check for the non pepeating 
        # character  
        while (not q.empty()):  
            if (charCount[ord(q.queue[0]) - ord('a')] > 1):  
                q.get()  
            else: 
                print(q.queue[0], end = " ")  
                break
  
        if (q.empty()): 
            print(-1, end = " ")
    print() 

for i in range(int(input())):
    n=int(input())
    s=list(input().split())
    s="".join(s)
    firstnonrepeating(s)
    
    
