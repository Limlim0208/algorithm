메모:
> 반복문으로 돌리는 컬렉션을 반복 중에 수정하면 안 된다. 수정이 필요하면 `while + popleft()` 패턴을 쓴다.  
> 빈 시퀀스에 `max()`를 쓰면 `ValueError`(런타임 에러)가 난다. if로 조건을 확인할 때는 0인지를 먼저 확인할 것

# 접근 방법

## 힌트
`deque`에 (우선순위, 인덱스)를 같이 넣고, 꺼낼 때마다 `any(...)`나 `max(...)`로 남은 큐에 더 높은 우선순위가 있는지 확인

# deque 사용법

## deque를 for문으로 사용할 때 주의점

`for p in deq:` 로 순회하는 도중에 `deq`의 내용이 바뀌거나(append, popleft) 크기가 변하면 아래 에러가 난다.

```
RuntimeError: deque mutated during iteration
```

이 문제는 순회하면서 "뒤로 보내기(append)"와 "꺼내기(popleft)"를 계속 해야 하므로 **for로 deque 자체를 순회하는 방식과 맞지 않는다.**

## 해결 방안

### 1) `list(dq)`로 감싸서 순회하는 방법

```python
for item in list(dq):
    ...
```

 복사본은 **처음 찍어둔 스냅샷**이라, 반복 중 원본이 바뀌어도 복사본은 반영되지 않는다.
- 뒤로 보낸 프로세스를 **다시 꺼내야** 하는 이 문제에는 한 번 훑는 것으로 부족하다. → 이 문제엔 부적합

### 2) `copy.deepcopy(dq)`로 딥 카피하는 방법

```python
import copy

for item in copy.deepcopy(dq):
    ...
```

- 1)과 같은 이유로 스냅샷 순회라서 이 문제의 의도와 맞지 않는다.
- 원소까지 전부 복사하므로 1)보다 비용도 크다. 순회 중 원소를 건드릴 일이 없다면 `list(dq)`로 충분하다.

### 3) `while dq:` + `dq.popleft()`를 쓰는 방법 

```python
while dq:
    item = dq.popleft()
    ...
```

- 매번 **현재 큐 상태**에서 새로 꺼내므로 "꺼낸다 → 판단한다 → 뒤로 보내거나 실행한다"를 그대로 옮길 수 있다.
- 순회 대상을 바꿔야 하면 **while + pop 패턴**으로 기억하기. (list, dict, set도 순회 중 수정 금지는 비슷하다.)


## 더 간단한 코드: `deque(enumerate(...))` + `any(...)`

```python
from collections import deque

def solution(priorities, location):
    answer = 0
    deq = deque(enumerate(priorities))  # (인덱스, 우선순위)

    while deq:
        i, p = deq.popleft()
        if any(p < q for _, q in deq):   # 남은 것 중 더 높은 게 있으면
            deq.append((i, p))           # 뒤로
        else:
            answer += 1                  # 실행
            if i == location:
                return answer
```

- 큐 만드는 부분: `for`문 + `append` 대신 `deque(enumerate(priorities))` 한 줄로 끝난다. 단, 튜플이 **(인덱스, 우선순위)** 순서로 들어가니까 꺼낼 때 `i, p` 순서를 맞춰야 한다.
- 비교 부분: `deq and max(...) > item[0]` 대신 `any(...)` 하나로 해결된다.
- `item[0]`, `item[1]` 대신 `i, p`로 풀어서 받으면 읽기도 편하다.

## `any(...)`

`any(iterable)`: 원소 중 **하나라도 True면 True**, 전부 False이거나 **비어 있으면 False**를 반환한다.  
(반대로 `all`은 전부 True여야 True이고, 비어 있으면 True)

```python
any([False, False, True])   # True
any([False, False])         # False
any([])                     # False  (빈 경우에도 에러 없음)

any(p < q for _, q in deq)  # 남은 큐에 p보다 큰 우선순위 q가 하나라도 있는지 확인
```

**`max` 방식과 비교**

| | `deq and max(t[0] for t in deq) > item[0]` | `any(p < q for _, q in deq)` |
| --- | --- | --- |
| 빈 큐 | `deq and` 로 따로 막아야 함 (안 하면 ValueError) | 에러 없이 `False` |
| 동작 | 매번 큐 **전체**를 훑어 최댓값을 구함 | 더 높은 것을 **하나 찾는 순간 멈춤** (단락 평가) |
| 의미 | "최댓값이 나보다 큰가?" | "나보다 큰 게 하나라도 있나?" |

- 이 문제는 "최댓값이 얼마인지"가 아니라 "더 높은 게 **있는지**"만 알면 되니까 `any`가 질문과 더 정확히 대응한다.
- 제너레이터를 그대로 넘기므로 `any([...])`처럼 리스트로 만들 필요 없이 `any(... for ... in ...)`로 쓴다. (`max`와 달리 `default`도 필요 없음)


## 참고: 알아두면 좋은 deque 메서드

| 메서드 | 설명 |
| --- | --- |
| `append(x)` | 오른쪽(뒤)에 추가 |
| `appendleft(x)` | 왼쪽(앞)에 추가 |
| `pop()` | 오른쪽에서 꺼냄 |
| `popleft()` | 왼쪽에서 꺼냄 (큐의 dequeue) |

- `pop()`을 쓰면 스택(DFS), `popleft()`를 쓰면 큐(BFS)처럼 동작한다.
