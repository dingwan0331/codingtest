# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/12930?language=python3

def solution(str):
  answer = ''
  count = 0
  for i in str:
    if i == ' ':
      answer += ' '
      count = 0
      continue
    answer += i.upper() if count % 2 == 0 else i.lower()
    count += 1
  return answer

'''
count 는 단어 별 index 역할을 한다
" " <- 이와같은 띄어 쓰기를 만나면 index를  의미하는 count를 초기화
띄어쓰기가 아닐 시에는 count가 홀수 일시 대문자 짝수일시 소문자를 answer에 추가
'''