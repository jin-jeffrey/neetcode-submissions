class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        remaining_stack = []
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while remaining_stack:
                compare_index = remaining_stack.pop()
                if temperatures[compare_index] < temp:
                    result[compare_index] = i - compare_index
                else:
                    remaining_stack.append(compare_index)
                    break
            remaining_stack.append(i)
        return result