# 접근1
> Stack
- stack 가장 위 `남은 일수`가 새로 들어온 `남은 일수`보다 작을 때 stack.pop()을 하는 방법

```
import math

def solution(progresses, speeds):
    answer = []
    dates=[]
    
    for n in range(len(progresses)):
        d=math.ceil((100-progresses[n])//speeds[n])

        if len(dates) != 0 and dates[-1]<d:
            count=0
            
             # while 작성 순서 중요!
            # 리스트가 빈 상태가 되면 dates[-1]을 평가하는 순간 이미 에러가 발생!!
            `
                dates.pop()
                count+=1
            answer.append(count)
        
        dates.append(d)
    answer.append(len(dates))
        
    return answer
```
## 문제
1. d 값이 내려갔다가 다시 애매하게 올라오는 경우는?
```
ex) d 배열이 [10, 3, 5] (예: progresses, speeds를 그렇게 맞춘 경우)라고 해봅시다.

첫 번째(10): 그룹 시작, dates=[10]
두 번째(3): dates[-1]=10 < 3? 거짓 → if문 안 들어가고 그냥 dates=[10, 3]
세 번째(5): dates[-1]=3 < 5? 참! → 여기서 flush 발생, 3만 pop하고 count=1로 answer에 append

근데 실제로는 세 기능 모두 그룹의 실제 배포일(=10)보다 작거나 같으니 전부 한 번에([3]) 배포돼야 맞습니다. 그런데 코드는 dates[-1] (방금 들어온 값 3)만 보고 비교하는 바람에, "그룹 전체의 배포일(현재까지의 최댓값)"이 아니라 "직전에 들어온 원소 하나"와만 비교하게 돼요. 그래서 원래 한 그룹이어야 할 게 쪼개집니다.
```

# 접근2
> Queue
- 생각해보니까 LIFO인 stack보다는 FIFO인 queue가 개념에 더 잘 맞음
- queue[0]과 d를 비교하도록 수정
- d 계산식을 `/`이 아니라 `//`으로 작성해서 `math.ceil` 계산이 효과가 없는 상태였음;;

## 해결책
```
import math

def solution(progresses, speeds):
    answer = []
    queue=[]
    
    for n in range(len(progresses)):
        # 각 작업별 남은 일수 d
        d=math.ceil((100-progresses[n])/speeds[n])

        if len(queue) != 0 and queue[0]<d:
            count=0

            while len(queue) != 0: 
                del queue[0]
                count+=1
            answer.append(count)
            
        queue.append(d)
    answer.append(len(queue))
        
    return answer
```

# 다른 접근
- 큐/리스트 없이 푸는 방법
```
import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    deploy_day = days[0]
    count = 0

    for d in days:
        if d <= deploy_day:
            count += 1
        else:
            answer.append(count)
            deploy_day = d
            count = 1

    answer.append(count)
    return answer
```
- d 계산을 리스트 컴프리헨션으로 한 줄에 미리 다 구해둠 (days)
- queue 자체를 없애고, "현재 그룹의 배포일"을 뜻하는 deploy_day, "현재 그룹 인원수"를 뜻하는 count 변수 두 개로만 로직을 표현
- 큐에 쌓았다가 while로 비우는 대신, 그냥 조건이 깨지는 순간 answer.append(count) 하고 새 그룹을 시작

# 메모
1. `while` 조건식에서 `while dates[-1] <= d and len(dates) != 0:`처럼 list의 마지막 항을 검사하고 list의 길이를 검사하는 순서로 코드를 작성했는데, index 오류가 났다.
**리스트의 길이가 0일 때 list[-1]을 검사하기만 해도 오류가 난다.** 그러니 리스트의 길이를 검사하고 항을 검사하는 순서(`while len(dates) != 0 and dates[-1] <= d:`)로 식을 써야 한다!!
__조건문 작성 순서에 주의하자.__

2. 큐 구현하기 참고 자료
https://velog.io/@gnwjd309/python-queue

3. 파이썬 소수점 올림, 내림 함수
```
import math

# 소수점 올림, 내림
math.ceil(2.1) # 3
math.floor(2.9) # 2
```

참고 자료: 
https://blockdmask.tistory.com/524

4. 들여쓰기 때문에 오류난 경우가 너무 많았다... 구문 주의
5. 꼭 자료구조를 안 써도 되는 경우는 사용하지 않는 편이 코드와 계산이 더 단순하다... 스택/큐로 분류되어 있어서 자료구조 개념을 계속 사용해서 풀려고 했는데 굳이 그러지 않아도 됐을 것 같음.
