class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        freq = {}
        #visited = set()
        result = []
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    count +=1
                else:
                    break
            freq[i]= count
        for i in range(k):
            min_index = -1
            min_value = float('inf')
            for key in freq:
                if freq[key] < min_value and (key not in result):
                    min_index = key
                    min_value = freq[key]
            result.append(min_index)
        return result
            