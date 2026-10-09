def solution(sizes):
    w=[]
    h=[]
    for i in range(len(sizes)):
        sizes[i].sort()
    for i in range(len(sizes)):
        w.append(sizes[i][0])
        h.append(sizes[i][1])
    return max(w)*max(h)