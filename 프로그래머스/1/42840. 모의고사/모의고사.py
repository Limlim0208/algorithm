# 1번 사람: 1, 2, 3, 4, 5 반복
# 2번 사람: 2, 1, 2, 3, 2, 4, 2, 5 반복
# 3번 사람: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 반복

def solution(answers):
    first=0
    second=0
    third=0
    max_score=0
    
    for i in range(len(answers)):
        if answers[i]==[1,2,3,4,5][i%5]:
            first+=1
        if answers[i]==[2, 1, 2, 3, 2, 4, 2, 5][i%8]:
            second+=1
        if answers[i]==[3, 3, 1, 1, 2, 2, 4, 4, 5, 5][i%10]:
            third+=1
    max_score=max(first, second, third)
    
    answer=[i+1 for i in range(3) if max_score == [first, second, third][i]]
    
    return answer