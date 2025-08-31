class TimeMap:

    def __init__(self):
        self.map ={} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [[value],[timestamp]]
        else:
            self.map[key][0].append(value)
            self.map[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        stamps = self.map[key][1]
        if timestamp >= stamps[-1]:
            return self.map[key][0][-1]
        if timestamp < stamps[0]:
            return ""
        l,r = 0,len(stamps)-1

        while (l<r):
            mid = (l+r)//2
            if stamps[mid] == timestamp:
                return self.map[key][0][mid]
            elif stamps[mid] < timestamp:
                l=mid+1
            elif stamps[mid] > timestamp:
                r=mid
        return self.map[key][0][l - 1] if l > 0 else ""