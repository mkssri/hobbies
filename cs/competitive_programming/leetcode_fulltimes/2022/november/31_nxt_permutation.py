class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def swap( idx1,idx2 ):
            tmp = nums[idx1]
            nums[idx1] = nums[idx2]
            nums[idx2] = tmp 
        
        def reverse( beg,end ):
            
            while( beg<end ):
                swap(beg,end)
                beg += 1
                end -= 1
        

        dec = n-2
        while( dec>=0 and nums[dec]>=nums[dec+1] ):
            dec -= 1

        reverse( dec+1,n-1 )

        if dec==-1:
            return

        nxt_num = dec+1
        while( nxt_num<=n-1 and nums[nxt_num]<=nums[dec]):
            nxt_num += 1
        
        swap(nxt_num,dec)