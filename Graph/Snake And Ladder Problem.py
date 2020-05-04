

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    snake={}
    ladder={}
    visited=set()
    que=[]
    for i in range(0,2*n,2):
        if arr[i]>arr[i+1]:
            snake[arr[i]]=arr[i+1]
        else:
            ladder[arr[i]]=arr[i+1]
    visited.add(1)
    que.append((1,0))
    
    while len(que):
        box,depth=que.pop(0)
        if box==30:
            print(depth)
            break
        for i in range(1,7):
            if( box+i not in visited and box+i>=1 and box+i<=30 ):
                if box+i in snake:
                    visited.add(box+i)
                    que.append((snake[box+i],depth+1))
                elif box+i in ladder:
                    visited.add(box+i)
                    que.append((ladder[box+i],depth+1))
                else:
                    visited.add(box+i)
                    que.append((box+i,depth+1))
