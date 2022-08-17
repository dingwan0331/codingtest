# 1137. N-th Tribonacci Number
# problem url = https://leetcode.com/problems/n-th-tribonacci-number/

# 재귀방식 시간초과
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)

# 시간은 패스한것
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        list1 = [0,1,1]
        for i in range(n-3):
            list1.append(sum(list1[i:]))
        return sum(list1[-3:])

# Dequeque 방식 을  list로 구현
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        list1 = [0,1,1]
        for i in range(n-3):
            list1.append(sum(list1))
            list1.pop(0)
        return sum(list1)