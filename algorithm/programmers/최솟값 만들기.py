# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    
    while B:
        answer += A.pop(0) * B.pop()
    return answer

def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    i = 0
    
    while B:
        answer += A[i] * B.pop()
        i += 1
    return answer

def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in A:
        answer += i * B.pop()
        
    return answer