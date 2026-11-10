# 최초 접근 방법
| 네트워크 개수를 DFS안에서 세는 구조
```
answer = 0

def DFS(computers,i,visited):
    global answer

    visited[i]=True
    for n, l in enumerate(computers[i]):
        if not visited[n] and l:
            DFS(computers, n, visited)
        else:
            answer+=1
            break

def solution(n, computers):
    visited=[False]*n
    DFS(computers,1,visited)

    return answer
```
문제: 해당 문제는 DFS가 개수를 세는 게 아니라 한 네트워크를 통째로 방문처리하는 역할을 해야 함.

- 시작점에서 갈 수 있는 모든 경우/노드만 보면 되면 → main 함수에 DFS 한 번 시작
 - ex) 한 시작점에서의 방문 순서 출력 같은 그래프가 하나로 이어져있다고 보장되는 경우
- 전체에 몇 덩어리가 있는지, 떨어진 것까지 전부 확인해야 하면 → 반복문으로 안 간 노드마다 DFS 시작
  - ex) 섬의 개수, 네트워크 개수 같은 연결 요소 세기 문제

다른 문제들
- `else: answer += 1`: "연결 안 됐거나 이미 방문한 칸"을 만날 때마다 실행되어서 네트워크가 끝났다는 뜻이 아님.
-`break`: 이웃 확인도 중단됨
- 시작 노드가 1번 하나뿐: 다른 네트워크는 DFS를 시작조차 안함

# 정답 코드

```
def solution(n, computers):
    visited=[False]*n
    answer=0
    
    for i in range(n): # 모든 컴퓨터를 하나씩 확인
        if not visited[i]: # 아직 방문하지 않은(어떤 네트워크에도 속하지 않은) 컴퓨터면
            DFS(computers, i, visited)# 그 네트워크 하나를 통째로 방문 처리
            answer+=1 # 네트워크 개수+1
    
    return answer

def DFS(computers,i,visited):
    visited[i]=True
    for j in range(len(computers)): # 한 노드에서 연결되어 있는 노드 순차 확인
        if computers[i][j] == 1 and not visited[j]: # ex) 1번 노드에서 2번 노드가 연결되어 있고, 2번 노드를 방문하지 않았으면
            DFS(computers, j, visited) # 이어서 탐색 진행
```

`if computers[i][j] == 1 and not visited[j]:` 연결되어 있는지 이렇게 표현하는 거 간단하고 너무 좋은 듯.
