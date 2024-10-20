class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(a,b):
            return a**2 + b**2
        heap = []
        for a,b in points:
            d = dist(a,b)
            if len(heap) < k:
                heapq.heappush(heap,(-d,a,b))
            else:
                heapq.heappushpop(heap,(-d,a,b))
        return [(a,b) for d,a,b in heap]