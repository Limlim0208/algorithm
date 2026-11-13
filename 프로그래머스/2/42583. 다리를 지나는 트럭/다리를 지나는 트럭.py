from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_que=deque([0]*bridge_length)
    truck_weights_que=deque(truck_weights)
    
    while truck_weights_que:
        time+=1
        bridge_que.popleft()
        if sum(bridge_que)+truck_weights_que[0]<=weight:
            bridge_que.append(truck_weights_que[0])
            truck_weights_que.popleft()
        else:
            bridge_que.append(0)
            
    return time+bridge_length