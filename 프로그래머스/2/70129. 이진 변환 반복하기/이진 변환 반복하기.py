def solution(s):
    c=0
    zero_count=0
    bin_count=0
    
    while c != 1:
        c=s.count("1")
        zero_count+=len(s)-c
        s=bin(c)[2:]
        bin_count+=1
        
    return [bin_count, zero_count]