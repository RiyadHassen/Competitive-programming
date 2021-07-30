class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.map_sum = []  
        # self.map = {}
        self.d = {}
    def insert(self, key: str, val: int) -> None:
        # array = [key,val]
        # self.map_sum.append(array)
        # self.map[key] = len(self.map_sum) -1
        self.d[key] = val

    def sum(self, prefix: str) -> int:
         return sum(self.d[i] for i in self.d if i.startswith(prefix))