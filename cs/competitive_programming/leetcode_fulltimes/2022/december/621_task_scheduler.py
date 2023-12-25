class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        res = len(tasks)
        char_map = [0]*26
        for e in tasks:
            char_map[ord(e)-ord('A')] += 1

        char_map.sort()
        max_ele = char_map[25]-1

        idle_slots = max_ele*n

        for i in range(24,-1,-1):
            idle_slots -= min(max_ele, char_map[i])
        
        if idle_slots>0:
            res += idle_slots
        
        return res
    
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        store = collections.defaultdict(int)
        for task in tasks:
            store[task] += 1

        max_heap = []

        for val in store.values():
            heapq.heappush(max_heap, -1*val)

        cycles = 0
        while(len(max_heap)!=0):
            tmp = []
            for i in range(n+1):
                if(len(max_heap)!=0):
                    tmp.append(heapq.heappop(max_heap))
            
            for e in tmp:
                if(-e-1>0):
                    heapq.heappush(max_heap,e+1)
            
            if(len(max_heap)==0):
                cycles += len(tmp)
            else:
                cycles += (n+1)

        return cycles