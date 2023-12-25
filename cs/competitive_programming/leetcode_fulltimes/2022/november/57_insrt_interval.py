class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):

            # *---N--*  *----* *---*
            if(newInterval[1] < intervals[i][0]):
                res.append(newInterval)
                res = res + intervals[i:]
                return res
            # *-----*  *--N--*
            elif(newInterval[0]>intervals[i][1]):
                res.append(intervals[i])
            #overlapping case
            else:
                newInterval[0] = min(newInterval[0],intervals[i][0])
                newInterval[1] = max(newInterval[1],intervals[i][1])

        res.append(newInterval)
        return res

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res=[]
        for i in range(len(intervals)):

            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res = res + intervals[i:]
                return res
            
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            
            else:
                newInterval[0] = min(newInterval[0],intervals[i][0])
                newInterval[1] = max(newInterval[1],intervals[i][1])
        
        res.append(newInterval)
        return res


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # newInterval
        # [n1 n2] [i[0] i[1]]..........

        # newInterval
        # [i[0] i[1]].......... [n1 n2]

        # newInterval overlapping
        # [i[0] i[1]].[i[2] [n1...n2] i[3]]......

        # newInterval
        # [i[0] i[1]] [n1 n2] [i[2] i[3]] .........


        res = []

        for i in range(len(intervals)):

            if newInterval[-1] < intervals[i][0]:
                res.append(newInterval)
                res += intervals[i:]
                return res

            elif intervals[i][-1] < newInterval[0]:
                res.append(intervals[i])
            
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[-1] = max(newInterval[-1], intervals[i][-1])
        
        res.append(newInterval)
        return res
