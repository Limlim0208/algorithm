def solution(arr, query):
    answer = []
    for i in range(len(query)):
        if i%2==0: # 짝수
            arr=arr[0:query[i]+1]
        else: # 홀수
            arr=arr[query[i]:]
            
    return arr