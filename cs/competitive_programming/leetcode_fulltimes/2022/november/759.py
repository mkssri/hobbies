from heapq import *

# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        result = []
        heap = [ (emp[0].start, idx, 0) for idx, emp in enumerate(schedule) ]
        heapq.heapify(heap)
        
        # either take end or the start of the starting interval
        # minStart = schedule[heap[0][1]][0].end
        minStart = heap[0][0]
        
        while heap:
            t, e_id, colIdx = heapq.heappop(heap)
            
            if minStart < t:
                result.append(Interval(minStart, t))
                
            minStart = max(minStart, schedule[e_id][colIdx].end)
            
            if colIdx + 1 < len(schedule[e_id]):
                colIdx += 1
                heapq.heappush(heap, (schedule[e_id][colIdx].start, e_id, colIdx))
        
        return result


schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
obj = Solution()
res = obj.employeeFreeTime(schedule)
print( "res: {}".format(res) )