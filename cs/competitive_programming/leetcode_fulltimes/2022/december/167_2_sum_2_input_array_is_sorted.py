from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if(len(numbers)==2):
            if target==(numbers[0]+numbers[1]):
                return [1,2]

        def bin_search(num, idx):
            l=idx+1
            r=len(numbers)-1
            if(l>r): return False

            while(l<=r):
                m=l+(r-l)//2
                ele=numbers[m]

                if(ele<num):
                    l=m+1
                elif(ele>num):
                    r=m-1
                else:
                    return m
            return False

        
        for i in range(len(numbers)):
            num_to_find=target-numbers[i]
            res=bin_search(num_to_find, i)     
            if res:
                return [i+1,res+1]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i,j=0,len(numbers)-1

        while i<j:
            total=numbers[i]+numbers[j]
            if(total>target):
                j-=1
            elif(total<target):
                i+=1
            else:
                return[i+1,j+1]