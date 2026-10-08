class TimeMap:

    def __init__(self):
        self.timestamp = defaultdict(list) # key : [(value, timestamp)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp:
            return ""
        
        lst = self.timestamp[key]

        if timestamp < lst[0][1]:
            return "" 

        l, r = 0, len(lst) - 1

        while l < r:
            m = (l + r + 1) // 2 

            if lst[m][1] == timestamp:
                return lst[m][0]
            elif lst[m][1] > timestamp:
                r = m - 1
            else:
                l = m
        
        return lst[l][0]


        
