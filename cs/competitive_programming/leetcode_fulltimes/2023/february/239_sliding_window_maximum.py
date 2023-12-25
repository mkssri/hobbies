#BRUTE FORCE TLE

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        # if n<=3:
        #     return [nums[0]]

        res = []

        for i in range(0,n-k+1):
            loop, m = k, 0
            tmp=[]
            while(m<loop):
                tmp.append(nums[i+m])
                m += 1
            res.append(max(tmp))

        return res
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # O(N) 
        # Monotonically decreasing stack implementation...

        n = len(nums)
        l = r = 0
        res = []
        q = collections.deque([])


        while(r<n):

            while(q and nums[q[-1]]<nums[r]):
                q.pop()
            q.append(r)

            while(q and l>q[0]):
                q.popleft()
            
            if(r+1>=k):
                res.append(nums[q[0]])
                l+=1
            
            r += 1

        return res