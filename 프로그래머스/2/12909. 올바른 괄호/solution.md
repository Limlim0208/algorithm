python 예외처리 구문을 활용해 다음과 같이 단순화 가능
```
def solution(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0
```
