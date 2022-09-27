# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/70129?language=python3

def solution(s):
    answer = [0,0]
    s = list(s)
    while len(s) != 1:
        a = []
        
        for idx,value in enumerate(s):
            if value == '0':
                a.append(idx)
                
        answer[1] += len(a)
        answer[0] += 1
        
        for i in a[::-1]:
            s.pop(i)
            
        s = list(bin(len(s)).replace('0b',''))
    return answer