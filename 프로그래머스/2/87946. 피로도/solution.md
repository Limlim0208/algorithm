## 접근 방법
> 순열 라이브러리 사용 -> 모든 순서를 시도해보고, 그중 최댓값을 취함

**주의사항**  
`permutations(list)` 를 쓸 때 `result=list(permutations(iterable))`처럼 **작성하면 안됨**

- `[x]` : x 자체를 원소로 하는 리스트를 생성, x가 뭐든 간에 통째로 한 칸에 넣음
- `list(x)` : x를 하나씩 꺼내서 그 원소들로 리스트를 생성

올바른 사용 방법: `result=list(permutations(iterable)`

**코드 예시**
```
from itertools import permutations
dungeons = [[80,20],[50,40],[30,10]]

a = [permutations(dungeons)]
# → [<permutations 객체>]          원소 1개짜리 리스트 (이터레이터가 통째로 들어감)

b = list(permutations(dungeons))
# → [([80,20],[50,40],[30,10]), ([80,20],[30,10],[50,40]), ...]   원소 6개짜리 리스트
```
---

# DFS 풀이방법

## 1. 개념
**DFS** 깊이 우선 탐색(Depth-First Search)  
어떤 노드부터 시작해서 인접한 노드들을 재귀적으로 방문해서 방문한 정점은 다시 방문하지 않고 각 분기마다 가능한 가장 멀리 있는 노드까지 탐색하는 알고리즘

**DFS 기본 원칙**
- `앞으로 가야할 노드`와 `이미 방문한 노드`를 기준으로 데이터 탐색

##  2. 스택/큐를 활용한 DFS 구현

### (1) 리스트(스택)를 활용한 DFS 구현
> `need_visited`에서 추가된 Node들 중 가장 끝에 있는 것을 뽑아서 검색하는 방법  
단점: list에서 pop을 활용하면 성능면에서 떨어짐

```
def dfs(graph, start_node):
 
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()
 
    ## 시작 노드를 시정하기 
    need_visited.append(start_node)
    
    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:
 
        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()
        
        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
 
            ## 방문한 목록에 추가하기 
            visited.append(node)
 
            ## 그 노드에 연결된 노드를 
            need_visited.extend(graph[node])
            
    return visited
```

### (2) deque를 활용한 DFS 구현 
> 논리는 거의 동일하지만 성능면에서 list() 형태보다 deque 형태가 훨씬 좋음

```
def dfs2(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()
    
    ##시작 노드 설정해주기
    need_visited.append(start_node)
    
    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.pop()
 
        ##만약 방문한 리스트에 없다면
        if node not in visited:
 
            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
                
    return visited
```

## 3. 재귀함수를 통한 DFS 구현
> visited 자료형을 기본 함수 인자로 포함, 방문한 리스트들을 재귀함수를 통해서 계속 visited에 담는 방식

```
def dfs_recursive(graph, start, visited = []):
## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
    visited.append(start)
 
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited
```


### 풀이 코드
```
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons): # k: 현재 피로도, cnt: 지금까지 돈 던전 수
    global answer
    if cnt > answer: # 1. 지금까지 돈 개수로 최댓값 갱신
        answer = cnt

    for j in range(N):  # 2. 모든 던전을 후보로 훑어봄
        if k >= dungeons[j][0] and not visited[j]: # 3. 입장 가능 + 아직 안 간 던전이면
            visited[j] = 1 # 4. 방문 표시
            dfs(k - dungeons[j][1], cnt + 1, dungeons) # 5. 그 던전을 돈 상태로 다음 선택 진행
            visited[j] = 0 # 6. 방문 표시 해제 (되돌리기)


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
```

### 참고자료
- permutations (https://blog.naver.com/hunii123/222322576767)
- DFS (https://data-marketing-bk.tistory.com/entry/DFS-%EC%99%84%EB%B2%BD-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
