class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.action = 0
        self.last_used = {}
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.action += 1
        self.last_used[key] = self.action
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.action += 1
        if key not in self.cache and len(self.cache.keys()) == self.capacity:
            min_value = float('inf')
            key_to_remove = -1
            # get key based on min value
            for k, v in self.last_used.items():
                if v < min_value:
                    min_value = v
                    key_to_remove = k
            del self.cache[key_to_remove]
            del self.last_used[key_to_remove]
        self.last_used[key] = self.action
        self.cache[key] = value
