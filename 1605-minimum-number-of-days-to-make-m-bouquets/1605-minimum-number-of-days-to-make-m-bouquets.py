class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(arr, day, m, k):
            n = len(arr)  # size of the array
            cnt = 0
            noOfB = 0
            # Count the number of bouquets
            for i in range(n):
                if arr[i] <= day:
                    cnt += 1
                    if cnt == k:  # Form a bouquet
                        noOfB += 1
                        cnt = 0
                else:
                    cnt = 0
            return noOfB >= m

        def roseGarden(arr, m, k):
            totalFlowersNeeded = m * k
            n = len(arr)  # size of the array
            if totalFlowersNeeded > n:
                return -1  # Impossible case

            # Find the minimum and maximum days in bloomDay
            low, high = min(arr), max(arr)

            # Apply binary search
            while low <= high:
                mid = (low + high) // 2
                if possible(arr, mid, m, k):
                    high = mid - 1  # Try smaller days
                else:
                    low = mid + 1  # Try larger days
            return low

        return roseGarden(bloomDay, m, k)