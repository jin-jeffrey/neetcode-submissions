import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        for i in tokens:
            if i.lstrip("-").isdigit():
                numbers.append(int(i))
            else:
                second = numbers.pop()
                first = numbers.pop()
                if i == "+":
                    numbers.append(first + second)
                elif i == "-":
                    numbers.append(first - second)
                elif i == "*":
                    numbers.append(first * second)
                else:
                    numbers.append(int(first / second))
        return numbers.pop()