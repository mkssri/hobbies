class Solution:
    def reorganizeString(self, s: str) -> str:

        # Use Heap
        """
        pop 2 elements at once, put them side by side
        and reinsert them to heap if ele freq still exists
        """

        # Building dictionary of items
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        # Adding elements to heap
        # python has only minheap implementation

        h = []
        from heapq import heappush, heappop

        for (k,v) in d.items():
            heappush(h, (-v,k))

        res = ""
        while len(h) > 1:

            freq1, ele1 = heappop(h)
            freq2, ele2 = heappop(h)

            res += ele1
            res += ele2

            if abs(freq1) > 1:
                heappush(h, (1+freq1,ele1))

            if abs(freq2) > 1:
                heappush(h, (1+freq2,ele2))

        if h != []:
            freq_f, ele_f = h[0]

            if abs(freq_f) > 1:
                return ""
            else:
                return res+ele_f
        else:
            return res