class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        for_dist = 0
        move = start
        while move != destination:
            for_dist += distance[move]
            move = move + 1
            if move == len(distance):
                move = 0 
        back_dist = 0
        move = start
        while move!= destination:
            move = move -1
            if move < 0:
                move = len(distance)-1
            back_dist += distance[move]
        return min(for_dist,back_dist)