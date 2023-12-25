class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -1*stones[i]

        heapq.heapify(stones)

        while(len(stones)>=2):

            ele1 = heapq.heappop(stones)
            ele2 = heapq.heappop(stones)

            if ele1==ele2:
                continue
            else:
                tmp = -ele1+ele2
                heapq.heappush(stones, -1*tmp)
        if(len(stones)==1):
            return -1*stones[0]
        else:
            return 0