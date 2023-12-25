from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        even_lst, odd_lst = [], []
        
        for x in nums:
            
            if x % 2 == 0:
                even_lst.append(x)
            else:
                odd_lst.append(x)
        
        
        # Join both lsts
        
        even_lst = even_lst + odd_lst
            
        
        print(even_lst)
        return even_lst
                