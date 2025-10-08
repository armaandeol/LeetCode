class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        temp = []
        potions.sort()
        def find_first_valid(potions, spell, success):
            low, high = 0, len(potions) - 1
            ans = len(potions)
            while low <= high:
                mid = (low + high) // 2
                if potions[mid] * spell >= success:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        for i in spells:
            idx = find_first_valid(potions, i, success)
            temp.append(len(potions) - idx)
        return temp