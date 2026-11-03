class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key, []) + [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])

        left = 0
        right = len(values) - 1
        latest_value = ""
        while left <= right:
            middle = (right + left) // 2

            if values[middle][0] > timestamp:
                right = middle - 1
            elif values[middle][0] <= timestamp:
                latest_value = values[middle][1]
                left = middle + 1
        return latest_value
