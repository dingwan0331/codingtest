#####[카카오 인턴]키패드 누르기 최초정답#######
def solution(numbers, hand):
    answer = ''
    hand = hand[0].upper()     # right left의 거리가 공통일경우 문자열을 치환할 손을 주어진 인자에서 띠왔습니다.
    # template = {1:[1,1],2:[2,1],3:[3,1],4:[1,2],5:[2,2],6:[3,2],7:[1,3],8:[2,3],9:[3,3],0:[2,4]}
    template = { i-4 : divmod(i,4) for i in range(5,14)}
    template.setdefault(0,(2,4))     
    # template.setdefault('R',[3,4])
    # template.setdefault('L',[1,4])
    '''
    dictionary representation을 사용하여 조금더 계산식으로써 템플릿을만들었습니다.
    0의 경우에는 예외적으로 처리하였습니다.
    '''
    R = 10
    L = 12
    # 오른손 왼손 default 좌표값입니다. # and *의 좌표값
    for i in numbers:
        if i ==0:
            numbers[numbers.index(i)] = 11
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            template['L'] = i
        elif i in [3,6,9]:
            answer += 'R'
            template['R'] = i
        else:
            if abs(i-R) == abs(i-L):
                answer += hand
                if hand =='R':
                    R = i
                else:
                    L = i
            elif abs(i-R) < abs(i-L):
                answer += 'R'
                R = i
            else:
                answer += 'L'
                L = i


    
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
    '''
    a = { str(i-4) : divmod(i,4) for i in range(5,16)}

    for i in numbers:
        if template[i][0]  == 1:
            answer += 'L'
            template['L'] = template[i]
        elif template[i][0] == 3:
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
                '''                
    return answer

'''  문제!!!
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

'''