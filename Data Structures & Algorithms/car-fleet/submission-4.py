class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # use a dictionary for position: time
        # build a stack from that
        position_time_dict = {}
        for i in range(len(position)):
            position_time_dict[position[i]] = (target - position[i]) / speed[i]
        position_time_items = sorted(position_time_dict.items(), key=lambda item: item[0], reverse=True)
        times = []
        for _, time in position_time_items:
            if times:
                previous_time = times.pop()
                times.append(previous_time)
                if previous_time < time:
                    times.append(time)
            else:
                times.append(time)
        return len(times)
