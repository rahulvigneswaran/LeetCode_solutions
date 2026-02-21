class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-1*i for i in counts.values()]
        heapq.heapify(maxHeap)
        q = deque()

        t = 0
        while maxHeap or q:
            t += 1

            if maxHeap:
                task = 1 + heapq.heappop(maxHeap)

                if task < 0:
                    q.append((task, t + n))
            else:
                t = q[0][1]

            if q and q[0][1] == t:
                task = q.popleft()
                heapq.heappush(maxHeap, task[0])
            
        return t

            


        
    