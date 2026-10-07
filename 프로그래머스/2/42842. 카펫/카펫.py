import math

def solution(brown, yellow):
   
    wh=brown+yellow # w*h
    s=0.5*(brown+4) # w+h
    
    x1 = 0.5*(s+math.sqrt(s**2-4*wh))
    x2 = 0.5*(s-math.sqrt(s**2-4*wh))
    
    return sorted([x1, x2], reverse=True)