def DFS(computers,i,visited):
    visited[i]=True
    for j in range(len(computers)):
        if computers[i][j] == 1 and not visited[j]:
            DFS(computers, j, visited)

def solution(n, computers):
    visited=[False]*n
    answer=0
    
    for i in range(n):
        if not visited[i]:
            DFS(computers, i, visited)
            answer+=1
    
    return answer