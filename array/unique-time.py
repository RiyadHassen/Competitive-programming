class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        result = [0]*(k)
        unique_value = {}
        for log in logs:
            if log[0] not in unique_value:
                unique_value[log[0]]=set()
                unique_value[log[0]].add(log[1])
            else:
                unique_value[log[0]].add(log[1])
        print(unique_value)
        for value in unique_value:
            result[len(unique_value[value])-1]+=1
        return result