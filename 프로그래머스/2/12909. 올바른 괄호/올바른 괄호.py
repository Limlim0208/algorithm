# 스택으로 구현, 괄호를 열때 push, 괄호를 닫을 때 pop으로 처리

def solution(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if not(len(stack)):
                return False
            else:
                stack.pop()
    if len(stack)!=0:
            return False
    return True