from collections import deque

def solution(maps):
    answer = 0
    
    # 최초 좌표(0,0) 목표 좌표(n-1,m-1)
    n = len(maps) #행
    m = len(maps[0]) #열
    
    visited = [[False]*m for _ in range(n)]
    answer=BFS(0,0, n,m,maps, visited)
    
    return answer

def BFS(start_row, start_col, n, m, maps, visited):
    
    
    # [0]:오른쪽, [1]:왼쪽, [2]:아래, [3]: 위 
    x=[1,-1,0,0]
    y=[0,0,1,-1]
    
    queue = deque([(start_row, start_col, 1)])
    visited[start_row][start_col]=True
    
    while queue:
        row, col, dist=queue.popleft()
        for i in range(4):
            new_row=row+y[i]
            new_col=col+x[i]
            if 0<=new_row<=n-1 and 0<=new_col<=m-1:
                if maps[new_row][new_col] and not visited[new_row][new_col]:
                    visited[new_row][new_col]=True
                    queue.append([new_row, new_col, dist+1])
                    
                    if new_row==n-1 and new_col==m-1:
                        return dist+1
    return -1
    
                
    
    