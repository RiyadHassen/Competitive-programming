def minimumRecolors(self, blocks: str, k: int) -> int:
        minOper = float('inf')
        left,right =0,0
        white = 0
        while right < len(blocks):
            if blocks[right]== 'W':
                white += 1
            if (right - left)+ 1== k:
                minOper = min(white,minOper)
                if blocks[left] ==  'W':
                    white -=1
                left+=1
                right += 1
                continue
            right+=1
        return minOper