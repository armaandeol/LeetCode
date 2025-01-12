class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        current = 1
        i = 0

        while missing_count < k:
            if i < len(arr) and arr[i] == current:
                i += 1
            else:
                missing_count += 1
                if missing_count == k:
                    return current
            current += 1

        return -1