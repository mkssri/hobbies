#!/usr/bin/python3

# Link - https://leetcode.com/problems/find-the-town-judge/

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        # EDGE CASE
        if n == 1 and len(trust) == 0:
            return n

        # trust.sort(key=lambda trust: trust[1])
        # print(trust)
        
        judge_dict = {}
        non_judge_lst = []
        
        for x in trust:
            
            if x[0] not in non_judge_lst:
                non_judge_lst.append(x[0])
        print("non_judge_lst - {}".format(non_judge_lst))
        
        if len(non_judge_lst) == n:
            return -1

        for x in trust:
            
            if x[1] not in non_judge_lst and x[1] not in judge_dict.keys():
                judge_dict[x[1]] = [x[0]]
            elif x[1] not in non_judge_lst:
                judge_dict[x[1]].append(x[0])
                
        print("judge_lst - {}".format(judge_dict))

        
        for x in judge_dict.keys():
            
            if (len(judge_dict[x])) == n-1:
                return x

        return -1
            

    

if __name__ == "__main__":
    
    obj = Solution()
    
    n = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    out = obj.findJudge(n, trust)
    print("ANS - {}".format(out))
    
    n = 2
    trust = [[1,2]]
    out = obj.findJudge(n, trust)
    print("ANS - {}".format(out))
    
    n = 3
    trust = [[1,3],[2,3]]
    out = obj.findJudge(n, trust)
    print("ANS - {}".format(out))
    
    n = 3 
    trust = [[1,3],[2,3],[3,1]]
    out = obj.findJudge(n, trust)
    print("ANS - {}".format(out))
    
    n = 3 
    trust = [[1,2],[2,3]]
    out = obj.findJudge(n, trust)
    print("ANS - {}".format(out))
