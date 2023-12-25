class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        store = {
            0:0
        }
        n = len(nums)

        c_sum = 0
        for i in range(n):
            c_sum += nums[i]
            store[c_sum] = i

        s_a_sum = c_sum-x

        c_val = 0
        l = 0

        for i in range(n):
            c_val += nums[i]
            l_sum = c_val-s_a_sum
            
            if(l_sum in store):

                if l_sum == 0:
                    l = max( l, i-store[l_sum]+1 )
                else:
                    l = max( l, i-store[l_sum] )
        
        if l == 0:
            if s_a_sum==0:
                return n
            else:
                return -1
        else:
            return n-l