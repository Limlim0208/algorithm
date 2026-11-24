def solution(nums):
    d= {}
    cnt=0
    length=len(nums)
    
    for n in nums:
        d[n]=d.get(n, 0)+1
    for k,v in d.items():
        if v>0:
            cnt+=1
    
    if cnt>length*0.5:
        return length*0.5
    else:
        return cnt