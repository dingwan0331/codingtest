######최초 정답 코드########
def solution(numbers, hand):
    answer = ''
    hand = hand[0].upper()
    dict1 = {1:[1,1],2:[2,1],3:[3,1],4:[1,2],5:[2,2],6:[3,2],7:[1,3],8:[2,3],9:[3,3],0:[2,4]}
    
    R = [3,4]
    L = [1,4]
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            L = dict1[i]
        elif i in [3,6,9]:
            answer += 'R'
            R = dict1[i]
        else:
            if abs(abs(dict1[i][0]-R[0])+abs(dict1[i][1]-R[1])) == abs(abs(dict1[i][0]-L[0])+abs(dict1[i][1]-L[1])):
                answer += hand
                if hand == 'R':
                    R = dict1[i]
                else:
                    L = dict1[i]
            elif abs(abs(dict1[i][0]-R[0])+abs(dict1[i][1]-R[1])) < abs(abs(dict1[i][0]-L[0])+abs(dict1[i][1]-L[1])):
                answer += 'R'
                R = dict1[i]
            else:
                answer +='L'
                L = dict1[i]
    return answer