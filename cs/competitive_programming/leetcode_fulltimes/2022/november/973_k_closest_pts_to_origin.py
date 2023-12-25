class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        n = len(points)
        points_lst = []

        for (x,y) in points:
            d = math.sqrt( math.pow(x,2) + math.pow(y,2) )
            points_lst.append((-1*d,[x,y]))

        print(points_lst)

        from heapq import heappush,heappop
        h = []

        for idx in range(k):
            heappush( h, points_lst[idx] )

        for idx in range(k, n):
            if points_lst[idx][0] > h[0][0]:
                heappop(h)
                heappush( h,points_lst[idx] )



        res = []

        for idx in range(k):
            res.append(h[idx][1])
        
        return res
    
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def calDistance(x,y):
            return math.sqrt(x**2+y**2)


        min_heap = []

        for point in points:
            d = calDistance(point[0],point[1])
            min_heap.append((-d,point))
        
        heapq.heapify(min_heap)

        while(len(min_heap)>k):
            heapq.heappop(min_heap)
        res=[]
        for ele in min_heap:
            res.append(ele[1])

        return res