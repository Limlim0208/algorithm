from itertools import permutations

def check(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    num_set=set()
    
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            num_set.add(int("".join(p)))
    
    for n in num_set:
        if n < 2: continue
        
        if check(n):
            answer+=1
        else: continue
    
    return answer