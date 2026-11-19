def solution(n, lost, reserve):
    answer = 0
    students=[1]*n
    for l in lost:
        students[l-1]-=1
    for r in reserve:
        students[r-1]+=1
        
    for i in range(n):
        if students[i]==0:
            if i>0 and students[i-1]==2:
                students[i-1]-=1
                students[i]+=1
            elif i<n-1 and students[i+1]==2:
                students[i+1]-=1
                students[i]+=1
                
    answer=sum(1 for s in students if s)
    return answer

# 1. n 길이 만큼 1을 가진 리스트를 만든다. [1]*5
# 2. for l in lost:
#    list[l-1]-=1
# for r in reserve:
#   list[r-1]-=1
# ex) [2,0,2,0,2]
# 1안) 2인 사람의 앞 뒤에 0이 있는지 검사, 그 사람에게 +1
# 2안) 0인 사람의 앞 뒤에 2인 사람이 있는지 검사, +1

