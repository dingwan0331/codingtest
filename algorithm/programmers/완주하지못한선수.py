############ 반쪽짜리 정답 ############
def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    return participant[0]

'''
나름 짧고 간결했지만 효율성 검사에서 0점 맞았습니다.
제가 생각할 수 있는 효율이라고는 이미 답이 나왔을때 무의미한 반복을 하지 않는것이기에 while문을 이용해 보았습니다.
'''

############# 성공한 정답 ############
def solution(participant, completion):
    try:
        answer = ''
        participant.sort()
        completion.sort()
        while True :
            answer = participant.pop()
            b = completion.pop()
            if answer != b:
                break
        return answer
    except:
        return answer

'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
'''

