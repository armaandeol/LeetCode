class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for start,end, time in roads:
            graph[start].append((time,end))
            graph[end].append((time,start))

        distance = [float('inf')] * n
        ways = [0] * n

        distance[0] = 0
        ways[0] = 1


        heap = [(0,0)]

        while heap:
            current,node = heapq.heappop(heap)

            if current > distance[node]:
                continue

            for time,end in graph[node]:
                if current + time < distance[end]:
                    distance[end] = current + time 
                    ways[end] = ways[node]
                    heapq.heappush(heap, (distance[end], end ))
                elif current + time == distance[end]:
                    ways[end] = ways[end] + ways[node]

        return ways[n-1] % (10**9 + 7)