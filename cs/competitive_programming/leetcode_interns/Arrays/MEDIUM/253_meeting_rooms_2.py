#!/usr/bin/python3

# Link - https://leetcode.com/problems/kth-largest-element-in-an-array/
# Youtube Solution - https://www.youtube.com/watch?v=tNhiD4SaumY


from typing import List
import random

"""
TIME COMPLEXITY - O(N*Log(N))
Worst case SPACE COMPLEXITY - O(N)
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # Sorting based on index0 of LIST        
        intervals.sort(key=lambda x : x[0])
        meeting_rooms = 1
        
        heap = [intervals[0][1]]
        
        for start,end in intervals[1:]:
            # heap[0] gives always minimum element
            if heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            
            meeting_rooms = max(meeting_rooms, len(heap))

        return meeting_rooms        
    

if __name__ == "__main__":
    
    obj  = Solution()
    intervals = [[0,30],[5,10],[15,20]]
    
    out = obj.minMeetingRooms(intervals)
    print("Minimum number of rooms required are - {}".format(out))
    