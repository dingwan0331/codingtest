#####문제######
'''
두 개의 input에는 복소수(complex number)가 string 으로 주어집니다. 복소수란 a+bi 의 형태로, 실수와 허수로 이루어진 수입니다.

input으로 받은 두 수를 곱해서 반환해주세요. 반환하는 표현도 복소수 형태의 string 이어야 합니다.

복소수 정의에 의하면 (i^2)는 -1 이므로 (i^2) 일때는 -1로 계산해주세요.

제곱 표현이 안 되어 i의 2제곱을 (i^2)라고 표현했습니다.
'''


#################최초 정답#################
def complex_number_multiply(a, b):
    tuple1 = a.replace('i','').split('+')
    tuple2 = b.replace('i','').split('+')
    list1 = []
    for i in tuple1:
        for j in tuple2:
            list1.append(int(i)*int(j))
    a = list1[0]-list1[-1]
    b = list1[1]+list1[2]
    return str(a)+'+'+str(b)+'i'

##############이쁘게 수정한 답안##############
def complex_number_multiply(a, b):
  a1,a2 = map(int, a.replace('i','').split('+'))
  b1,b2 = map(int, b.replace('i','').split('+'))  
  return '{0}+{1}i'.format((a1*b1 + -a2*b2),(a2*b1 + a1*b2))
