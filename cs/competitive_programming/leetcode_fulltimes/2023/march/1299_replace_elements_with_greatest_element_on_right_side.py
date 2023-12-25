class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0]*n
        ans[-1] = -1

        for i in range(n-2,-1,-1):
            ans[i] = max(ans[i+1], arr[i+1])

        return ans

# TLE
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n = len(arr)

        for i in range(n-1):
            tmp = arr[i+1]
            for j in range(i+2, n):
                tmp = max(tmp, arr[j])
            arr[i] = tmp
        arr[-1] = -1
        return arr
