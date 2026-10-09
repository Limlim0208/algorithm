## 더 간단한 코드
> w = 각 명함 사각형에서 작은 값을 찾고, 개중 가장 큰 값을 return  
> h = 각 명함 사각형에서 큰 값을 찾고, 개중 가장 큰 값을 return
```
def solution(sizes):
    w = max(min(s) for s in sizes)
    h = max(max(s) for s in sizes)
    return w * h
```
## 최댓값을 갱신하는 방식
> 리스트를 만들지 않고 w,h에 바로 최댓값을 갱신
```
def solution(sizes):
    w = h = 0
    for a, b in sizes:
        w = max(w, min(a, b))
        h = max(h, max(a, b))
    return w * h
```
