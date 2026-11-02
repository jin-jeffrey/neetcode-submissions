import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search for the min eating speed, start with the max value in the list
        lower_limit_speed = 1
        upper_limit_speed = max(piles)
        min_eating_speed = max(piles)
        while lower_limit_speed <= upper_limit_speed:
            eating_speed = (upper_limit_speed + lower_limit_speed) // 2
            total_time = 0
            for pile_size in piles:
                total_time += math.ceil(pile_size / eating_speed)
            if total_time <= h:
                upper_limit_speed = eating_speed - 1
                min_eating_speed = min(eating_speed, min_eating_speed)
            else:
                lower_limit_speed = eating_speed + 1
        return min_eating_speed