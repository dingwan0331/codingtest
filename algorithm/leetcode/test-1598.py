# 1598. Crawler Log Folder
# problem url = https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for i in logs:
            if i =='../':
                if result ==0:
                    pass
                else:
                    result -= 1
            elif i =='./':
                result += 0
            else:
                result += 1
        return result