class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        set_candies = set(candies)
        max_ele = max(set_candies)

        res = []
        for i in range(len(candies)):
            if(candies[i]+extraCandies >= max_ele):
                res.append(True)
            else:
                res.append(False)
        return res