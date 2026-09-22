import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        indexed_tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        res = []
        min_heap = []
        i = 0
        n = len(tasks)
        current_time = 0
        
        while len(res) < n:
            while i < n and indexed_tasks[i][0] <= current_time:
                heapq.heappush(min_heap, (indexed_tasks[i][1], indexed_tasks[i][2]))
                i += 1
            
            if not min_heap:
                current_time = indexed_tasks[i][0]
            else:
                proc_time, index = heapq.heappop(min_heap)
                current_time += proc_time
                res.append(index)
                
        return res