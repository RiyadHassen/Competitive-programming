class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []
        for (a,b) in classes:
            max_heap.append(((a/b-(a+1)/(b+1)),a,b))
        
        heapq.heapify(max_heap)
        
        for _ in range(extraStudents):
            profit,a,b = heapq.heappop(max_heap)
            a,b = a+1,b+1
            heapq.heappush(max_heap,(-(a+1)/(b+1)+a/b,a,b))
        return sum(a/b for _,a,b in max_heap)/len(max_heap)
        
        