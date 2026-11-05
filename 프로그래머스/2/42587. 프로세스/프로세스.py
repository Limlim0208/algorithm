from collections import deque

def solution(priorities, location):
    answer = 0
    deq=deque()
    
    for i, p in enumerate(priorities):
        deq.append((p,i)) # 우선순위, 인덱스
        
    while deq:
        item = deq.popleft()
        # 큐에 있는 프로세스를 하나씩 뽑아서 확인
        
        if deq and max(p[0] for p in deq) > item[0]:
            deq.append(item)
        else:
            answer+=1
            if item[1]==location:
                return answer
