def solution(brown, yellow):
    total=brown+yellow
    
    for w in range(int(total**0.5), total):
        if total % w == 0:
            h=total//w
            if brown == (2*w+2*h-4):
                return sorted([w,h], reverse=True)