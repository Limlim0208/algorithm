어렵다...

참고한 풀이
- https://school.programmers.co.kr/questions/93528
- https://school.programmers.co.kr/questions/86313
- https://jhzlo.tistory.com/71  


i마다 for range(n)으로 검사하는 이유
  ```
      for i in range(n):
        next_idx=i+1
        
        while next_idx < n and name[next_idx]=="A":
            next_idx+=1
        
        move=min(move, i*2+(n-next_idx), (n-next_idx)*2+i)
  ```
-> 어느 A 묶음을 건너뛸 때 가장 이득인지 찾기 위해
