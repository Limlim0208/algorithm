> 메모: answer을 list로 만들고, len(list)로 정답을 return하려고 애를 썼는데 차라리 소수인지만 확인하고 answer에 +1을 해주는 게 훨씬 간단했다...  
> 필요 시 새로운 함수를 정의해서 solution에 호출하는 게 코드가 깔끔해진다.  
> 문제 풀이에 필요한 패키지를 알아두는 것도 필요해 보인다. `itertools.permutations`을 모르고 구현을 하려고 시도했는데 너무 어려워서 포기했다...

### 코드 풀이 참고 자료
파이썬 풀이 https://school.programmers.co.kr/questions/92467

# 접근 방법

## `itertools.permutations`

`combinations(iterable, r)` : iterable에서 원소 개수가 r개인 조합 뽑기
```
from itertools import permutations

list(permutations("17", 1))  # [('1',), ('7',)]
list(permutations("17", 2))  # [('1', '7'), ('7', '1')]
```

### 참고 자료
https://blog.naver.com/hunii123/222322576767

## 소수 판별 알고리즘

### 1. N을 2부터 N-1까지 나눠보기

 2부터 N-1 까지의 수로 해당 수를 나눠보고, 이 과정에서 어떠한 수에 의해 나누어 떨어지는지 확인한다.  
나누어떨어지지 않는다면 해당 수는 소수인 것이고, 도중에 다른 수에 의해 나누어 떨어진다면 그 수는 소수가 아닐 것이다.

**예시코드**
```
def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴
    
    return True # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴
```

시간복잡도: O(N)

### 2. 약수의 특성 활용하기

특정 수 N의 약수들을 일렬로 나열했을 때 그 중 가운데의 수를 중심으로 약수가 대칭된다.

**예시**
16의 약수: 1, 2, 4, 8, 16  
중간값 4를 기준으로 약수들이 서로 대칭된다. (1 * 16 = 16 * 1, 2 * 8 = 8 * 2)  
-> 16의 약수를 찾고 싶다면, 16의 약수의 중간값을 기준으로 한 쪽만 검사를 하더라도 다른 쪽의 약수를 찾을 수 있다.

중간값= N의 제곱근 값으로 가정할 수 있음.  
이 제곱근 값을 기준으로 왼쪽에 약수가 하나도 존재하지 않는다면, 제곱근 값 기준 오른쪽에도 약수가 존재하지 않는다고 확신할 수 있다.

이를 통해 우리는 기존 for문이 2에서 N-1까지 돌았던 것을 2에서 N의 제곱근까지만 돌도록 처리해주어 연산 횟수를 절반에 가깝게 줄여줄 수 있다.

**예시코드**

```
def is_prime_num(n):
    for i in range(2, int((n)**0.5)+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True
```

### 에라토스테네스의 체

여러 수에 대해서 소수 판별을 해줘야하는 상황에서 사용  
ex. 100~300 사이의 모든 소수들을 구해야 함

**에라토스테네스의 체 알고리즘의 작동방식**
1. 2 ~ N까지의 범위가 담긴 배열을 만든다.
2. 해당 배열 내의 가장 작은 수 i 부터 시작하여, i의 배수들을 해당 배열에서 지워준다. (i는 소수이기 때문에 i자체는 지우지 않는다.)
3. 주어진 범위 내에서 i의 배수가 모두 지워지면 i 다음으로 작은 수의 배수를 같은 방식으로 배열에서 지워준다.
4. 더 이상 반복할 수 없을 때까지 2, 3번의 과정을 반복해준다.


예시코드
```
def is_prime_num(n):
    arr = [True] * (n + 1) # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True: # 특정 수가 지워지지 않았다면 (소수여서)
            j = 2

            while (i * j) <= n:
                arr[i*j] = False # i의 배수의 값을 False로 지워준다.
                j += 1

    return arr

arr = is_prime_num(50) # 0 ~ 50중 소수를 구하기 위한 함수

for i in range(len(arr)):
    if arr[i] == True:
        print(i, end=' ')
```

약수의 특징을 이용한 예시코드
```
import math

def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1

    return arr

arr = is_prime_num(50)

for i in range(len(arr)):
    if arr[i] == True:
        print(i, end=' ')
```


### 참고 자료
소수판별 알고리즘 - 파이썬 (Python) https://seongonion.tistory.com/43
