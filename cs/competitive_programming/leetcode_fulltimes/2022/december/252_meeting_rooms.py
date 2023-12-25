class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        # sample.sort(key = lambda i:i[1], reverse = True)
        intervals.sort(key=lambda i:i[0])


        for i in range(len(intervals)-1):
            end = intervals[i][1]
            nxt_start = intervals[i+1][0]

            if(end>nxt_start):
                return False
        return True