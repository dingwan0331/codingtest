#####[카카오 인턴]키패드 누르기 최초정답#######
def solution(numbers, hand):
    answer = ''
    hand = hand[0].upper()     # right left의 거리가 공통일경우 문자열을 치환할 손을 주어진 인자에서 띠왔습니다.
    # template = {1:[1,1],2:[2,1],3:[3,1],4:[1,2],5:[2,2],6:[3,2],7:[1,3],8:[2,3],9:[3,3],0:[2,4]}
    template = { i-4 : divmod(i,4) for i in range(5,14)}
    template.setdefault(0,(2,4))     
    template.setdefault('R',[3,4])
    template.setdefault('L',[1,4])
    '''
    dictionary representation을 사용하여 조금더 계산식으로써 템플릿을만들었습니다.
    0의 경우에는 예외적으로 처리하였습니다.
    '''
    # 오른손 왼손 default 좌표값입니다. # and *의 좌표값

    '''
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            L = template[i]
        elif i in [3,6,9]:
            answer += 'R'
            R = template[i]
        else:
            if abs(abs(template[i][0]-R[0])+abs(template[i][1]-R[1])) == abs(abs(template[i][0]-L[0])+abs(template[i][1]-L[1])):
                answer += hand
                if hand == 'R':
                    R = template[i]
                else:
                    L = template[i]
            elif abs(abs(template[i][0]-R[0])+abs(template[i][1]-R[1])) < abs(abs(template[i][0]-L[0])+abs(template[i][1]-L[1])):
                answer += 'R'
                R = template[i]
            else:
                answer +='L'
                L = template[i]
    '''

    for i in numbers:
        if template[i][0]  == 1 :
            answer += 'L'
            template['L'] = template[i]
        elif template[i][0] ==3:
            answer += 'R'
            template['R'] = template[i]
        else:
            if abs(abs(template[i][0]-template['R'][0])+abs(template[i][1]-template['R'][1])) == abs(abs(template[i][0]-template['L'][0])+abs(template[i][1]-template['L'][1])):
                answer += hand
                template[hand] = template[i]
            elif abs(abs(template[i][0]-template['R'][0])+abs(template[i][1]-template['R'][1])) < abs(abs(template[i][0]-template['L'][0])+abs(template[i][1]-template['L'][1])):
                answer += 'R'
                template['R'] = template[i]
            else:
                answer += 'L'
                template['L'] = template[i]
                
    return answer