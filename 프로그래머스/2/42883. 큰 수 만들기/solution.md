# 접근: stack 활용
- 새로 들어오는 숫자가 스택 맨 위에 있는 숫자보다 크면 그 위의 숫자를 제거하는 방식
> 문제: 시간초과, 일부 테스트케이스 실패
```
def solution(number, k):
    stack=[]
    
    for c in number:
        if len(stack)!=0:
            for n in reversed(stack):
                if (int(n)<int(c)) and (k!=0):
                    stack.pop()
                    k-=1
        stack.append(c)
    
    return ''.join(map(str, stack))
```

두 가지 문제
1. 시간 초과: 매 문자마다 revered(stack)으로 스택 전체를 훑고 있음.
2. 일부 테스트 케이스 실패: 문자열을 모두 순회했는데도 k!=0인 경우

## 해결책
```
def solution(number, k):
    stack=[]
    
    for c in number:
        while (len(stack)!=0) and (int(stack[-1])<int(c)) and (k!=0) :
            stack.pop()
            k-=1
        stack.append(c)
    if k!=0:
        stack=stack[0:-k]
    
    return ''.join(map(str, stack))
```
1. 비교할 대상은 스택의 맨 위 하나면 충분함. `for` 대신 `while`을 사용해서, 스택이 비어있지 않고+`k`가 남아있고+맨 위 원소(`stack[-1]`)가 새 숫자보다 작을 때만 반복해서 pop하는 방식으로 수정
2. 루프가 끝난 뒤에도 남은 `k`를 처리해주는 코드 추가
