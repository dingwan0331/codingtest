# 557. Reverse Words in a String III
# problem url = https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split(' ')
        result = ''
        
        for i in list1:
            result += i[-1::-1]
            result += ' '
            
        return result[:-1]