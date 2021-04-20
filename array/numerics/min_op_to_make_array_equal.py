class Solution:
    def minOperations(self, n: int) -> int:
        sum_item = 0
        result = 0
        for i in range(n):
            sum_item += ((2 * i)+1)
        sum_item = sum_item//n
        target = sum_item
        for i in range(1,target,2):
            result += (sum_item-i)
        return result