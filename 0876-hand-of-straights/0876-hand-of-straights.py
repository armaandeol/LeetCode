class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        freq = defaultdict(int)
        for card in hand:
            freq[card] += 1

        heap = list(freq.keys())
        heapq.heapify(heap)

        while heap:
            smallest = heap[0]
            for num in range(smallest,smallest+groupSize):
                if num not in freq:
                    return False
                freq[num] -= 1
                if freq[num] == 0:
                    if num != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True
        