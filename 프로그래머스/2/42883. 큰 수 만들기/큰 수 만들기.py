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