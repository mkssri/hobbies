class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start_lst, end_lst = [], []


        for idx in range(len(intervals)):
             start_lst.append(intervals[idx][0])
             end_lst.append(intervals[idx][1])

        start_lst.sort()
        end_lst.sort()

        s, e = 0, 0
        res, cnt = 0, 0

        while( s < len(start_lst) ):

            if(start_lst[s] < end_lst[e]):
                cnt += 1
                s += 1
            else:
                cnt -= 1
                e += 1
            res = max( res, cnt )

        return res 