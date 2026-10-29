def solution(m, n, puddles):
    puddle_set = {(y - 1, x - 1) for x, y in puddles}  # (행, 열)로 변환
    route=[[0]*m for _ in range(n)]
    route[0][0]=1
    
    for i in range(n):
        for j in range(m):
            if(i,j) in puddle_set:
                route[i][j]=0
                continue
            if i>0:
                route[i][j]+=route[i-1][j]
            if j>0:
                route[i][j]+=route[i][j-1]
            route[i][j]%=1000000007
            
    return route[n - 1][m - 1]