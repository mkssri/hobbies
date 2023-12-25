class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n1 = len(nums1)
        n2 = len(nums2)
        store = {}

        for i in range(n2):
            c_e = nums2[i]
            k = i+1
            while(k<n2):
                if c_e<nums2[k]:
                    store[c_e]=nums2[k]
                    break
                k+=1
            if c_e not in store:
                store[c_e]=-1


        ans = []
        for i in range(n1):
            c_e = nums1[i]
            ans.append(store[c_e])
        return ans
