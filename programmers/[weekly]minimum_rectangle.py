######[위클리챌린지]최소직사각형 나의 정답####
def solution(sizes):
    a = []
    b = []
    for i in sizes:
        a.append(min(i))
        b.append(max(i))
    answer = max(a)*max(b)
    return answer

##########짝꿍정답########
def solution(sizes):
    a,b = 0,0
    for i in sizes:
        a = max(a,i[0])
        b = max(a,i[1])
    return a*b