class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        for i in range(K):
            min_num = float('inf')
            min_index = float('inf')
            for j in range(len(A)):
                if A[j] < min_num:
                    min_num = A[j]
                    min_index = j
            if A[min_index]!=0:
                A[min_index] = -A[min_index]
        return sum(A)