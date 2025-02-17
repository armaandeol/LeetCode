class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        curr_time = 0
        heap = []
        for k,v in Counter(tasks).items():
            heappush(heap, (-1*v, k))
        while heap:
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if heap:
                    x,y = heappop(heap)
                    if x != -1:
                        temp.append((x+1,y))
                if not heap and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(heap, item)
        return curr_time