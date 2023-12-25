"""
Time Complexity: O(N+Q)
"""
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        n = len(s)
        prefix_sum, candle_s, candle_e = [0]*n, [n]*n, [-1]*n

        prefix_sum[0] = 1 if s[0]=="*" else 0        
        candle_e[0] =  1 if s[0] =='|' else -1
        candle_s[n-1] = n-1 if s[n-1]=='|' else n

        for idx in range(1, n):
            prefix_sum[idx] = prefix_sum[idx-1] + (1 if s[idx]=='*' else 0)
            candle_e[idx] =  idx if s[idx] =='|' else candle_e[idx-1]

        for idx in range(n-2, -1, -1):
            candle_s[idx] = idx if s[idx]=='|' else candle_s[idx+1]

        res = []
        for idx in range(len(queries)):

            st = candle_s[queries[idx][0]]
            end = candle_e[queries[idx][1]]

            res.append( 0 if st>=end else prefix_sum[end]-prefix_sum[st])

        return res
     
"""
TLE
Time Complexity: O(N*Q)
"""
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        res = []
        for q in queries:            
            res.append( self.compute(s[q[0]:q[1]+1]) )
        return res


    def compute( self, sub_str ):


        pl_cnt = 0
        s_pl_f, e_pl_f = False, False
        s_idx = 0
        e_idx = len(sub_str)-1

        for idx in range(0,len(sub_str)):
            if(sub_str[idx]=="|"):
                s_idx = idx
                s_pl_f = True
                break
        for idx in range(len(sub_str)-1,-1,-1):
            if(sub_str[idx]=="|"):
                e_idx = idx
                e_pl_f = True
                break

        if ( (s_pl_f and e_pl_f) and ( s_idx < e_idx ) ):
            for idx in range(s_idx+1,e_idx):
                if sub_str[idx] == "*":
                    pl_cnt += 1


        return pl_cnt