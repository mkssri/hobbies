from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        store=collections.defaultdict(list)
        res=[]
        n=len(nums)
        for i in range(len(nums)):
            store[nums[i]].append(i)
        
        for i in range(n):
            for j in range(i+1,n):
                tmp=nums[i]+nums[j]
                if -tmp in store:
                    for k in store[-tmp]:
                        if i!=k and j!=k:
                            to_add=[nums[i],nums[j],nums[k]]
                            to_add.sort()
                            if to_add not in res: res.append(to_add)

        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res_set=set()
        nums.sort()

        for i in range(len(nums)):
            target=-nums[i]
            s,e=i+1,len(nums)-1
            while(s<e):
                tmp=nums[s]+nums[e]
                if(tmp==target):
                    res_set.add((nums[i],nums[s],nums[e]))
                    s+=1
                elif(tmp<target):
                    s+=1
                else:
                    e-=1
        res=[]
        for ele in res_set:
            res.append(list(ele))
        return res