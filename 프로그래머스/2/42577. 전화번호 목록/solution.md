## 문제 설명
> `list phone_book`: 전화번호를 담은 배열  
> 어떤 번호가 다른 번호의 접두어인 경우가 있으면 `false` / 그렇지 않으면 `true`

**접근 방법**: 2중 for 문으로 앞에서부터 뒤에 자신을 접두어로 가지는 전화번호가 있는지 순서대로 확인  
**문제**: 뒤의 번호가 앞의 번호의 접두어인 경우 확인 불가

**수정 방향**: `phone_book`을 sort하면 사전순으로 정렬됨 -> 앞 뒤로 접두어 관계인 번호끼리 붙음  
-> 전체를 2중 for문으로 탐색하는 게 아니라 앞 번호가 뒤 번호의 접두어인지만 확인하면 OK

### 내 풀이
```
def solution(phone_book):
    phone_book.sort()

    n=len(phone_book)
    for i, p in enumerate(phone_book):
        if i+1<n and len(phone_book[i])<len(phone_book[i+1]) and phone_book[i+1][:len(phone_book[i])]== p:
            return False

    return True
```
**단점**: `list.sort()`이 최악의 경우 시간복잡도가 O(N log N)이라 시간이 오래 걸림

### 다른 사람 풀이
```
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
```
- `hash_map`에 전체 전화번호를 등록
- `phone_book`에 등록된 `phone_number`를 순차 탐색
  - `phone_number`의 번호를 앞에서부터 잘라서 `temp`에 이어붙임
  - `temp`가 `hash_map`에 있는지 확인, 자기 자신인 경우 제외
  - 즉, `phone_number`를 앞에서부터 한 글자씩 잘라서 자신의 접두어가 `hash_map`에 있는지 확인하는 방식
  -   있으면 `return False`
