class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue,count,course = deque([]),0,[]
        indgree,adj_list={},{}
        for pre in prerequisites:
            if pre[1] not in adj_list:
                adj_list[pre[1]]=[pre[0]]
            else:
                adj_list[pre[1]].append(pre[0])
        for i in range(numCourses):
            indgree[i]= 0 
        for pre in prerequisites:
            indgree[pre[0]]+= 1
        for dgree in indgree:
            if indgree[dgree]==0:
                queue.append(dgree)
        while queue:
            ele = queue.popleft()
            course.append(ele)
            count+=1
            if ele in adj_list:
                for child in adj_list[ele]:
                    indgree[child]-=1
                    if indgree[child]==0:
                        queue.append(child)
        if count==numCourses:
            return course
        return []
        