def solution(nums):
    d= {}
    cnt=0
    
    for n in nums:
        d[n]=d.get(n, 0)+1
        
    for n in d:
        if d[n]>0:
            cnt+=1
            
    return min(cnt, len(nums)/2)