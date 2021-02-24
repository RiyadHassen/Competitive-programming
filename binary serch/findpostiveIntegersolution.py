"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        for n in range(1,z+1):
            start = 1
            end = z
            while (start <= end):
                
                middle = start + (end-start)//2
                if customfunction.f(n,middle) == z:
                    result.append([n,middle])
                    break
                elif customfunction.f(n,middle) > z:
                    end = middle -1 
                else :
                     start = middle +1
                    
        return result
                    
                    
                    