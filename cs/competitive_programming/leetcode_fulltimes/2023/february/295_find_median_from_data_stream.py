class MedianFinder:
    
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:

        if(self.large and num>self.large[0]):
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1*num)
        
        if(len(self.small)>(len(self.large)+1)):
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if(len(self.large)>(len(self.small)+1)):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

        

    def findMedian(self) -> float:

        if len(self.large)>len(self.small):
            return self.large[0]
        elif len(self.small)>len(self.large):
            return -1*self.small[0]
        else:
            return (-1*self.small[0]+self.large[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



class MedianFinder:
    
    def __init__(self):
        self.store = []
        

    def addNum(self, num: int) -> None:
        self.store.append(num)
        

    def findMedian(self) -> float:
        n = len(self.store)
        self.store.sort()

        if(n%2==0):
            tmp = (self.store[n//2]+self.store[n//2-1])/2
            return tmp
        else:
            return self.store[n//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:

        if self.large and num>self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1*num)

        # Ordering
        if(self.small and self.large and ((-1*self.small[0]) > self.large[0])):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)
        
        l1 = len(self.small)
        l2 = len(self.large)

        if(l1>(l2+1)):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)
        if(l2>(l1+1)):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

    def findMedian(self) -> float:
        
        l1, l2 = len(self.small), len(self.large)

        if(l1<l2):
            return self.large[0]
        elif(l1>l2):
            return -1*self.small[0]
        else:
            return (self.large[0] + -1*self.small[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
