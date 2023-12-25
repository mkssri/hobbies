class HitCounter:
    
    def __init__(self):
        self.hits = collections.deque([])
        
    def hit(self, timestamp: int) -> None:
        if len(self.hits)==0:
            self.hits.append((timestamp,1))
        elif self.hits[-1][0] == timestamp:
            curr_cnt = self.hits[-1][1]
            self.hits[-1]=(timestamp,curr_cnt+1)
        else:
            self.hits.append((timestamp,1))

        
    def getHits(self, timestamp: int) -> int:

        target = timestamp-300
        
        while( len(self.hits) != 0 and self.hits[0][0]<=target ):
            self.hits.popleft()

        cnt = 0
        for (v,c) in self.hits:
            cnt += c
        return cnt 
"""
hit - Time Complexity: O(1)
getHits - Time Complexity: O(N)

#Space Complexity worst case - O(N)
"""

class HitCounter:
    
    def __init__(self):
        self.hits = []
        
    def hit(self, timestamp: int) -> None:
        self.hits.append( timestamp )
        
    def getHits(self, timestamp: int) -> int:
        left, right = 0, len(self.hits)-1
        target = timestamp-300

        while(left<=right):

            mid = left + (right-left)//2

            if(self.hits[mid] <= target):
                left = mid+1
            else:
                right = mid-1
        
        return len(self.hits)-left

"""
hit - Time Complexity: O(1)
getHits - Time Complexity: O(logN)

#Space Complexity - O(N)
"""
