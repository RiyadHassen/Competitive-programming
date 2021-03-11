class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left,right,maxlen = 0,0,0
        while right < len(s):
            cost = abs(ord(s[right])-ord(t[right]))
            if cost <= maxCost:
                maxCost -=cost
                right +=1
            else:
                maxlen=max(maxlen,(right-left))
                while cost > maxCost:
                    first = abs(ord(s[left])-ord(t[left]))
                    maxCost+=first
                    left += 1
        return max(maxlen,right-left)