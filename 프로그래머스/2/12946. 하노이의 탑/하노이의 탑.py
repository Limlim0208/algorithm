def solution(n):
    answer = []
    answer=hanoi(n, 1, 3, 2, answer)
    return answer

def hanoi(n, start, end, sub, answer):
    if n ==1:
        answer.append([start, end])
    else:
        hanoi(n-1, start, sub, end, answer)
        answer.append([start,end])
        hanoi(n-1, sub, end, start, answer)
    return answer