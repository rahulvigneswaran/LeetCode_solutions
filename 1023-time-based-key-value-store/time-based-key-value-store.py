class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        
        L, R = 0, len(self.storage[key]) - 1
        res = ""

        while L <= R:
            mid = L + (R-L)//2
            val, ts = self.storage[key][mid]
            
            if ts <= timestamp:
                res = val
                L = mid + 1
            else:
                R = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)