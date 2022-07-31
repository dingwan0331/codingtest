# 1047. Remove All Adjacent Duplicates In String

class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = [s[0]]              # 인자로받은 스트링의 가장 첫 요소를 result의 요소로 시작
        for i in s[1:]:              
            if len(result)>0:        # index error 방지용
                if result[-1] == i:  # result의 마지막 요소와 i가 같으면 == 중복요소
                    result.pop()     # result의 마지막 요소를 제거
                else:
                    result.append(i) # 같지않다면 result에 추가
            else:
                result.append(i)     # result의 길이가 0일때는 그냥 추가
        return ''.join(result)