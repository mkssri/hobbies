class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []
        for num in nums:
            min_heap.append(num)
        heapq.heapify(min_heap)

        while(len(min_heap)>k):
            heapq.heappop(min_heap)
        
        return min_heap[0]