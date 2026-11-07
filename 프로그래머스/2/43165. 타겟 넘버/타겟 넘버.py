def dfs(numbers, idx, total, target):
    if idx==len(numbers):
        if total==target:
            return 1
        return 0
    
    plus=dfs(numbers, idx+1, total+numbers[idx],target)
    minus=dfs(numbers, idx+1, total-numbers[idx], target)
    
    return plus+minus
    
def solution(numbers, target):
    return dfs(numbers, 0, 0,target)