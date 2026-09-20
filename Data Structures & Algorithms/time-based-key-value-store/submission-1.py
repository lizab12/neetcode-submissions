class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        i = 0
        j = len(self.store[key])-1
        n = self.store[key]
        res = ""
        while i<=j:
            mid = (i+j)//2
            if n[mid][1]<=timestamp:
                res = n[mid][0]
                i = mid +1
            else:
                j = mid -1
        return res
        
