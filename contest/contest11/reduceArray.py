class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}
        count = 0
        sum_value = 0
        half = len(arr)//2
        freq = Counter(arr)
        values = sorted(list(freq.values()))
        for i in range(len(values)-1, -1, -1):
            if sum_value >= half:
                break
            sum_value += values[i]
            count += 1
        return count
