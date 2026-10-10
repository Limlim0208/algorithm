## 접근
- `answers`의 인덱스를 기준으로 탐색할 때, 반복 패턴의 응답과 정답지가 같은 경우(`list[i%(패턴 개수)]==answers[i]`) 정답 개수(`first`, `second`, `third`)를 1씩 증가
- 가장 높은 점수를 받은 사람이 여럿일 경우를 처리하기 위해 `max_score`로 세 사람 중 가장 높은 점수를 저장해두었다가, `max_score`와 점수가 같은 사람을 `answer`에 포함해 `return`

### 리스트 컴프리헨션 참고자료
https://m.blog.naver.com/math717/224374290704
