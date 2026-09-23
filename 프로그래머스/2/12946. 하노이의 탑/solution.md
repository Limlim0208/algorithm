# 접근방식
**필요한 개념**
> 재귀

전체 과정 `hanoi(n)`을 `hanoi(n-1)`로 분리할 수 있다.

1. n-1개 원판을 1번 막대에서 2번 막대로 옮긴다.
2. 남은 1개 원판을 1번 막대에서 3번 막대로 옮긴다.
3. 다시 n-1개 원판을 2번 막대에서 3번 막대로 옮긴다.

*규칙에 따라 N번째 원판을 1번에서 3번으로 옮기려면, **1번째~N-1번째 원판이 모두 2번막대에 꽂혀있어야 함.**  
문제 정의에서 각 이동의 출발지와 목적지를 함께 기술해야 하기 때문에 이 두 정보+경유점까지 함께 받도록 함수를 구성한다.
```
# move(N, start, end): N번 원판을 start에서 end로 옮긴다.
# answer.append([start, end])로 정답에 포함

hanoi(N, start, end, sub)=
    n=1일 때, move(1, start, end) # if N == 1
    n!=1일 때, # else
        hanoi(N-1, start, sub, end)
        + move(N, start, end)
        + hanoi(N-1, sub, end, start)
```

### 참고자료
https://mgyo.tistory.com/185#google_vignette
