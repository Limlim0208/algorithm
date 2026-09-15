def solution(k, m, score):
    answer = 0
    score.sort()
    for i in range(len(score)//m):
        answer+=score[(len(score)%m+m*i)]*m
    return answer