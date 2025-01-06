class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(arr, day, m, k):
            n = len(arr)
            cnt = 0
            noOfB = 0    
            for i in range(n):
                if arr[i] <= day:
                    cnt += 1
                    if cnt == k:  
                        noOfB += 1
                        cnt = 0
                else:
                    cnt = 0
            return noOfB >= m

        def roseGarden(arr, m, k):
            totalFlowersNeeded = m * k
            n = len(arr)
            if totalFlowersNeeded > n:
                return -1

            
            low, high = min(arr), max(arr)

            
            while low <= high:
                mid = (low + high) // 2
                if possible(arr, mid, m, k):
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        return roseGarden(bloomDay, m, k)