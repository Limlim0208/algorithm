# list phone_book : 전화번호를 담은 배열
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false / 그렇지 않으면 true

# 접근 방법: 앞에서부터 뒤에 자신을 접두어로 가지는 전화번호가 있는지 순서대로 확인
# 문제: 뒤의 번호가 앞의 번호의 접두어인 경우 확인 불가

def solution(phone_book):
    phone_book.sort()

    n=len(phone_book)
    for i, p in enumerate(phone_book):
        if i+1<n and len(phone_book[i])<len(phone_book[i+1]) and phone_book[i+1][:len(phone_book[i])]== p:
            return False

    return True