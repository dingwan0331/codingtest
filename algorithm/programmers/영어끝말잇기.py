# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/12981

import math
def solution(n, words):
    a = []
    answer = []
    for idx,value in enumerate(words):
        if idx == 0:
            continue
        if words[idx-1][-1] != value[0]:
            answer.append(idx)
            break
        elif words.count(value) ==2:
            if not a.count(value):
                answer.append(idx)
                break
            else:
                a.append(value)
    if not answer:
        return [0, 0]
    return [n - (idx+1)%n, math.ceil((idx+1) /n)]
    
    answer = [num,count]
    return answer