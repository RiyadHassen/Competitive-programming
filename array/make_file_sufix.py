class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        uniques ={}
        result = []
        for name in names:
            if name not in uniques:
                uniques[name]=1
                result.append(name)
            else:
                small_val = uniques[name]
                temp = name +'('+str(small_val)+')'
                while temp in uniques:
                    small_val = small_val + 1
                    temp = name +'('+str(small_val)+')'                    
                uniques[temp] = 1
                uniques[name]+=1
                result.append(temp)
        return result
            