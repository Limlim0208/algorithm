def solution(s):
    
    list = [int(i) for i in s.split()]
    list.sort()
    
    return f'{list[0]} {list[-1]}'