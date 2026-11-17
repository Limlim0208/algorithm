from collections import deque

def solution(maps):
    answer = 0
    
    # 최초 좌표(0,0) 목표 좌표(n-1,m-1)
    n, m = len(maps),len(maps[0])  #행, 열
    visited = [[False]*m for _ in range(n)]
    
    # [0]:오른쪽, [1]:왼쪽, [2]:아래, [3]: 위 
    x_move=[1,-1,0,0]
    y_move=[0,0,1,-1]
    
    queue = deque([(0, 0, 1)])
    visited[0][0]=True
    
    while queue:
        y, x, d=queue.popleft()
        
        for i in range(4):
            ny=y+y_move[i]
            nx=x+x_move[i]
            
            if 0<=ny<=n-1 and 0<=nx<=m-1:
                
                if maps[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx]=True
                    queue.append([ny, nx, d+1])
                    
                    if ny==n-1 and nx==m-1:
                        return d+1
    return -1
    