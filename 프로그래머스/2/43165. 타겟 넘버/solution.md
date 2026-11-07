메모: 숫자마다 **+ 또는 − 두 가지 선택**이 있고, 모든 조합 중 target이 되는 개수를 세는 문제라 DFS(재귀)가 자연스럽다.  
> 처음엔 +/− 구분을 인자로 줘야 하나 헷갈렸는데, **부호는 이미 합에 반영된 결과**로 넘기면 돼서 인자는 `(idx, total)`이면 충분했다.
> **return 값 합산**과 **global 변수**를 사용해서 개수를 셀 수 있는데, `return`으로 푸니까 값이 어떻게 합산되는 건지 너무 헷갈려서 `global`이 더 직관적인 것 같다...

# 1. 주의 사항

- 제한 사항: 숫자 20개 이하 → 2²⁰ ≈ 100만 번 정도라 **전부 탐색해도 충분**하다.
- **`global`은 변수를 바꾸는 함수마다 따로** 써야 한다. `solution`에만 쓰고 `dfs`에 빼먹으면 아래 에러가 난다.
  ```
  UnboundLocalError: cannot access local variable 'answer' where it is not associated with a value
  ```
  - 파이썬은 함수 안에 `answer += 1` 같은 **대입**이 있으면 그 변수를 지역 변수로 취급한다. 그래서 바깥의 `answer = 0`을 못 본다.
  - 읽기만 할 때는 `global`이 없어도 되지만, **대입(`=`, `+=`)을 하면 꼭 필요**하다.
- `solution` 안에서 `answer = 0`으로 **초기화**해야 한다. 테스트케이스마다 `solution`이 여러 번 호출될 수 있어서, 초기화가 없으면 이전 케이스의 개수가 쌓인다.
- 정수 인자(`cnt` 등)를 함수 안에서 바꿔도 **호출한 쪽에는 반영되지 않는다.** 그래서 `cnt`를 인자로 넘겨서 누적하는 방식은 안 된다. (return 값 또는 global로 세야 함)
- 재귀 호출의 **반환값을 버리면 안 된다.** return 방식에서 `dfs(...)`만 호출하고 결과를 안 쓰면 `None`이 되어 `None + None` 에러가 난다.
- 시작 인덱스/합을 정할 때 숫자가 **중복으로 더해지지 않게** 주의. `idx=0, total=0`에서 시작하고, `idx`번째 숫자를 아직 안 쓴 상태로 정의하면 헷갈리지 않는다.

# 2. 접근 방법

## 힌트

각 숫자마다 +/− 두 갈래로 재귀 호출하고, 마지막 숫자까지 다 처리했을 때 합이 `target`과 같으면 방법 수를 1 늘린다.

## 풀이 흐름

1. `dfs(numbers, idx, total, target)`: idx번째 숫자부터 처리할 차례, 지금까지의 합이 total
2. 종료 조건: `idx == len(numbers)` (숫자를 전부 사용함)
   - `total == target` 이면 방법 +1
3. 아니면 두 갈래로 호출
   - `dfs(..., idx + 1, total + numbers[idx], ...)` (+ 선택)
   - `dfs(..., idx + 1, total - numbers[idx], ...)` (− 선택)
4. `solution`에서 `dfs(numbers, 0, 0, target)`으로 시작

## 예시 (numbers = [1, 1], target = 2)

```
dfs(idx=0, total=0)
├─ +1 → dfs(idx=1, total=1)
│   ├─ +1 → dfs(idx=2, total=2) → 2 == 2 → 방법 +1 ✅
│   └─ −1 → dfs(idx=2, total=0) → 0 != 2
└─ −1 → dfs(idx=1, total=-1)
    ├─ +1 → dfs(idx=2, total=0) → 0 != 2
    └─ −1 → dfs(idx=2, total=-2) → -2 != 2
→ 총 1가지
```

## 코드 1: global 변수

```python
answer = 0

def dfs(numbers, idx, total, target):
    global answer              # dfs에서도 answer를 바꾸니까 필요
    if idx == len(numbers):
        if total == target:
            answer += 1        # target을 만들었으면 +1
        return

    dfs(numbers, idx + 1, total + numbers[idx], target)   # + 선택
    dfs(numbers, idx + 1, total - numbers[idx], target)   # - 선택


def solution(numbers, target):
    global answer
    answer = 0                 # 테스트케이스마다 초기화
    dfs(numbers, 0, 0, target)
    return answer
```

## 코드 2: return 값 합산

```python
def dfs(numbers, idx, total, target):
    if idx == len(numbers):
        return 1 if total == target else 0      # 맨 끝에서 1 또는 0

    plus = dfs(numbers, idx + 1, total + numbers[idx], target)
    minus = dfs(numbers, idx + 1, total - numbers[idx], target)
    return plus + minus                         # 두 갈래의 개수를 합쳐서 위로


def solution(numbers, target):
    return dfs(numbers, 0, 0, target)
```

## DFS vs BFS 고르는 기준

- **최소/최단** (최단 거리, 최소 횟수) → BFS. 가까운 곳부터 퍼져서 처음 도착한 순간이 곧 최단이다.
- **모든 경우 / 몇 가지 / 가능한가** (경우의 수, 순열/조합, 백트래킹) → DFS. 재귀로 짜면 짧고 자연스럽다.
- 경우의 수 세기는 BFS로도 풀리지만 굳이 그럴 이유가 없다. 반대로 최단 거리를 DFS로 구하면 모든 경로를 비교해야 해서 비효율적이다.
