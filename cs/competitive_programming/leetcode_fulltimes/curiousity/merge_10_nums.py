class Solution:
    
    def mergeNums( self, nums ):
        
        res = nums[0]
        i = 1
        for num in nums[1:]:
            left_shift = 3*i
            num = num << left_shift
            i += 1
            res = res | num
            
        return res
    
    def getNums( self, res ):
        lst = []
        match = 7
        
        while( res >= 1 ):
            lst.append( res & match )
            res = res >> 3
            
        return lst
                
    def dec2bin( self, num ):
        
        if num == 0:
            return 0
        
        ans = ""
        while( num >= 1 ):
            b = num%2
            ans += str(b)
            num = num//2
        
        return ans[len(ans)::-1]

obj = Solution()
nums = [7,1,2,3,4,3,5,6,7,1]
print("Input nums: {}".format(nums))
res = obj.mergeNums(nums)

lst = obj.getNums( res )
print("lst: {}".format(lst))

"""
Input nums: [7, 1, 2, 3, 4, 3, 5, 6, 7, 1]
lst: [7, 1, 2, 3, 4, 3, 5, 6, 7, 1]
"""