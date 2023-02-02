class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        operation = 0
        while nums:
            # if len(heap) == 0:
            #     break
            min_num = nums[0]
            if min_num > 0:
                operation +=1
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] -= min_num
            while nums and nums[0] == 0:
                heapq.heappop(nums)
        return operation
                
                