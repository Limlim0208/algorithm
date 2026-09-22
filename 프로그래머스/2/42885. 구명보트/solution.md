#   접근1: 작은 순으로 태우기
> 문제: 작은 순으로만 태우는 경우 말고도 40, 60 으로 태우는 경우에도 limit보다 작은 구성이 생김
```
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    for _ in range(len(people)):
    
      if len(people)>=2:
          if people[-1]+people[-2] <= limit:
              people.pop()
              people.pop()
              answer+=1
          else:
              people.pop()
              answer+=1
      elif len(people)==1 :
          people.pop()
          answer+=1
      else:
          break

return answer
```

# 접근2: 맨 앞 가벼운 애랑 limit를 빼고 최대인 애를 같이 태움
> 문제: 시간초과가 뜸, 꼭 limit를 꽉 채우지 않더라도 limit-(가장가벼운 사람 몸무게) 이하인 사람도 태울 수 있어야 함
```
def solution(people, limit):
    answer = 0
    people.sort()
    
    while True:
        if limit-people[0] in people[1:]:
            people.pop(0)
            people.remove(limit-people[0])
            answer+=1
            if len(people)==0:
                break
        else:
            people.pop(0)
            answer+=1
            if len(people)==0:
                break
    
    return answer
```
# 접근3(정답): 투 포인터 접근
```
def solution(people, limit):
    answer = 0
    people.sort()
    
    left=0
    right=len(people)-1
    
    while left<=right:
        if left<right and people[left]<=limit-people[right]:
            left+=1
        right-=1
        answer+=1
    
    return answer
```
> 정렬 후 left는 가장 가벼운 사람, right는 가장 무거운 사람을 가리키게 합니다.  
> 매번 가장 무거운 사람(right)은 무조건 보트에 태웁니다 (어차피 누군가와 짝지어야 하고, 가장 무거우니 남은 사람 중 아무나와 태울 기회가 제일 적음).  
> 이때 가장 가벼운 사람(left)과 함께 태울 수 있는지(people[left] + people[right] <= limit) 확인해서, 가능하면 같이 태우고 left도 이동시킵니다. 불가능하면 무거운 사람 혼자 태웁니다.  
> right는 항상 한 칸씩 줄이고, left는 같이 탔을 때만 한 칸씩 늘리면서, left <= right일 동안 반복하고 보트 개수를 세면 됩니다.  

**주의**
- 가벼운 사람부터 태우는 게 아니라 무거운 사람부터 태우면, 가장 가벼운 사람과 같이 태웠을 때 limit를 벗어나면 바로 보트 개수를 +1할 수 있음
- `while` 조건은 `left<=right`로 두고, `left==right`인 조건을 걸러내기 위해 `if left<right **and** people[left]<=limit-people[right]` 조건문을 두어야 함

