class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        res = []
        visit_set = set()

        for ele in arr:
            if ele not in visit_set:
                cnt = arr.count(ele)
                res.append(cnt)
            visit_set.add(ele)

        res.sort()

        for idx in range(len(res)-1):

            c_ele = res[idx]
            n_ele = res[idx+1]

            if c_ele == n_ele:
                return False
        
        return True