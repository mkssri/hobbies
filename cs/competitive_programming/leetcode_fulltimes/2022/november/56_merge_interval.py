class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort( key=lambda i:i[0] )
        res = [ intervals[0] ]

        for start,end in intervals[1:]:

            last_end = res[-1][1]

            if start <= last_end:
                res[-1][1] = max(end,last_end)
            else:
                res.append([start,end])
        
        return res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda i:i[0])
        res = [ intervals[0] ]

        for s,e in intervals[1:]:
            l_e=res[-1][1]
            if(s<=l_e):
                res[-1][1]=max(l_e,e)
            else:
                res.append([s,e])
        return res
