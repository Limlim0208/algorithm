from itertools import permutations

def solution(k, dungeons):
    order=list(permutations(dungeons)) # 던전의 전체 순열
    answer=0
    
    for i, o in enumerate(order): # 던전 순서
        count=0 # 현재 던전 순서에서 돌고 있는 던전 개수
        current_k=k # 현재 피로도 리셋
        
        for d in o: # 각 던전을 순서대로 돎
            if current_k>=d[0]: # 현재 피로도 >= 최소 필요 피로도이면
                current_k-=d[1] # 현재 피로도-소모 피로도
                count+=1
            else:
                break
            
            answer = max(answer, count) # 지금까지 돈 던전 개수를 max로 갱신
    
    return answer