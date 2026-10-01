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