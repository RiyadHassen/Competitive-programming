class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        removed =set()
        size = 0 
        sort_orders = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        for item,value in sort_orders:
            if size >= (len(arr)//2):
                break
            removed.add(item)
            size = size + value 
        return len(removed)
    