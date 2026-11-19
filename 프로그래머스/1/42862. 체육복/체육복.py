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

